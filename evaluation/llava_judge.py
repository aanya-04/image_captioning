# """
# llava_judge.py

# Evaluates captions using LLaVA-1.5
# """

# import torch

# from models.llava_loader import load_llava_model
# from utils.preprocess import preprocess_image

# from evaluation.prompts import (
#     SYSTEM_PROMPT,
#     build_prompt
# )

# from evaluation.parser import parse_response


# class LlavaJudge:

#     def __init__(self):

#         self.processor, self.model = load_llava_model()

#     def evaluate(self, image_path, captions):

#         image = preprocess_image(image_path)

#         prompt = build_prompt(captions)

#         messages = [

#             {
#                 "role": "system",
#                 "content": SYSTEM_PROMPT
#             },

#             {
#                 "role": "user",
#                 "content": [

#                     {
#                         "type": "image"
#                     },

#                     {
#                         "type": "text",
#                         "text": prompt
#                     }

#                 ]
#             }

#         ]

#         text = self.processor.apply_chat_template(
#             messages,
#             tokenize=False,
#             add_generation_prompt=True
#         )

#         # print("=" * 100)
#         # print("LLaVA Prompt")
#         # print("=" * 100)
#         # print(prompt)
#         # print("=" * 100)

#         inputs = self.processor(
#             text=text,
#             images=image,
#             return_tensors="pt"
#         )

#         inputs = inputs.to(self.model.device)

#         with torch.no_grad():

#             generated_ids = self.model.generate(

#                 **inputs,

#                 max_new_tokens=800,

#                 do_sample=False,

#                 use_cache=True

#             )

#         generated_ids = generated_ids[
#             :,
#             inputs.input_ids.shape[1]:
#         ]

#         response = self.processor.batch_decode(

#             generated_ids,

#             skip_special_tokens=True,

#             clean_up_tokenization_spaces=False

#         )[0]

#         # print("=" * 100)
#         # print("LLaVA Response")
#         # print("=" * 100)
#         # print(response)
#         # print("=" * 100)

#         results = parse_response(response)

#         print("\nParsed Results:")
#         print(results)

#         valid_rows = {

#             item["row"]

#             for item in captions

#         }

#         filtered = []

#         for item in results:

#             row = item.get("row")

#             if row in valid_rows:

#                 filtered.append(item)

#             else:

#                 print(f"Skipping invalid row: {row}")

#         if len(filtered) != len(captions):

#             print()

#             print("Expected Rows :", sorted(valid_rows))
#             print("Returned Rows :", [r["row"] for r in filtered])

#             raise RuntimeError(
#                 "Invalid evaluation returned by LLaVA."
#             )

#         return filtered




"""
llava_judge.py

Evaluates captions using LLaVA-1.5
"""

import torch

from models.llava_loader import load_llava_model
from utils.preprocess import preprocess_image

from evaluation.prompts import (
    SYSTEM_PROMPT,
    build_prompt
)

from evaluation.parser import parse_response


class LlavaJudge:

    def __init__(self):

        self.processor, self.model = load_llava_model()

    def evaluate(self, image_path, captions):

        # -------------------------------------------------
        # Load image
        # -------------------------------------------------

        image = preprocess_image(image_path)

        # -------------------------------------------------
        # Build prompt
        # -------------------------------------------------

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
                        "type": "image"
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
            text=text,
            images=image,
            return_tensors="pt"
        )

        inputs = inputs.to(self.model.device)

        # -------------------------------------------------
        # Generate response
        # -------------------------------------------------

        with torch.no_grad():

            generated_ids = self.model.generate(

                **inputs,

                max_new_tokens=800,

                do_sample=False,

                use_cache=True

            )

        generated_ids = generated_ids[
            :,
            inputs.input_ids.shape[1]:
        ]

        response = self.processor.batch_decode(

            generated_ids,

            skip_special_tokens=True,

            clean_up_tokenization_spaces=False

        )[0]

        # -------------------------------------------------
        # Parse JSON
        # -------------------------------------------------

        results = parse_response(response)

        # -------------------------------------------------
        # Validate rows
        # -------------------------------------------------

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

        # -------------------------------------------------
        # Ensure every caption has exactly one evaluation
        # -------------------------------------------------

        if len(results) != len(captions):

            print("\nExpected Rows :", sorted(valid_rows))
            print("Returned Rows :", [r["row"] for r in results])

            raise RuntimeError(
                "LLaVA returned an invalid number of results."
            )

        # -------------------------------------------------
        # Check duplicate rows
        # -------------------------------------------------

        rows = [item["row"] for item in results]

        if len(rows) != len(set(rows)):

            raise RuntimeError(
                "Duplicate rows returned by LLaVA."
            )

        # -------------------------------------------------
        # Check duplicate ranks
        # -------------------------------------------------

        ranks = [item["rank"] for item in results]

        if len(ranks) != len(set(ranks)):

            raise RuntimeError(
                "Duplicate ranks returned by LLaVA."
            )

        # -------------------------------------------------
        # Sort by Excel row
        # -------------------------------------------------

        results.sort(
            key=lambda x: x["row"]
        )

        return results