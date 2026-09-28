import torch

from models.qwen_loader import load_qwen_model
from utils.preprocess import preprocess_image

from evaluation.prompts import (
    SYSTEM_PROMPT,
    build_prompt
)

from evaluation.parser import parse_response


class QwenJudge:

    def __init__(self):

        self.processor, self.model = load_qwen_model()

    def evaluate(self, image_path, captions):

        image = preprocess_image(image_path)

        prompt = build_prompt(captions)

        messages = [

            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },

            {
                "role": "user",
                "content": [

                    {
                        "type": "image",
                        "image": image
                    },

                    {
                        "type": "text",
                        "text": prompt
                    }

                ]
            }

        ]

        text = self.processor.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )

        inputs = self.processor(
            text=[text],
            images=[image],
            return_tensors="pt"
        )

        # inputs = {
        #     k: v.to(self.model.device)
        #     for k, v in inputs.items()
        # }

        inputs =inputs.to(self.model.device)

        with torch.no_grad():

            generated_ids = self.model.generate(

                **inputs,

                max_new_tokens=800,

                do_sample=False,

                temperature=None,

                use_cache=True

            )

        generated_ids = [

            output_ids[len(input_ids):]

            for input_ids, output_ids in zip(
                inputs.input_ids,
                generated_ids
            )

        ]

        response = self.processor.batch_decode(

            generated_ids,

            skip_special_tokens=True,

            clean_up_tokenization_spaces=False

        )[0]

        print("=" * 100)
        print(response)
        print("=" * 100)

        results = parse_response(response)

        valid_rows = {
            item["row"]
            for item in captions
        }

        filtered = []

        for item in results:

            if item["row"] in valid_rows:
                filtered.append(item)
            else:
                print(f"Skipping invalid row {item['row']}")

        results = filtered

        return results