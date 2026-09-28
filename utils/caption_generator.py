import torch
from utils.preprocess import preprocess_image

def generate_caption(
    processor,
    model,
    image_path,
    prompt
):

    MAX_NEW_TOKENS = 1200
    TEMPERATURE = 0.85
    TOP_P = 0.9
    # TOP_K=1000
    DO_SAMPLE = True
    USE_CACHE = True
    image = preprocess_image(image_path)

    messages = [
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

    text = processor.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    # print("=" * 80)
    # print(text)
    # print("=" * 80)

    inputs = processor(
        text=[text],
        images=[image],
        return_tensors="pt"
    )


   
   
    # if "pixel_values" in inputs:
    #     print("Pixel values shape:", inputs["pixel_values"].shape)

    inputs = {
        k: v.to(model.device)
        for k, v in inputs.items()
    }

    with torch.no_grad():

        generated_ids = model.generate (
            **inputs,
            max_new_tokens=MAX_NEW_TOKENS,
            do_sample=DO_SAMPLE,
            temperature=TEMPERATURE,
             top_p=TOP_P,
            # min_new_token = 500,
            # top_k = TOP_K,
            repetition_penalty=1.1,
            use_cache=USE_CACHE,
        )

        # generated_ids = model.generate(
        #     **inputs,
        #     max_new_tokens=MAX_NEW_TOKENS,
        #     do_sample=True,
        #     temperature=0.2,
        #     top_p=0.9,
        #     use_cache=True,
        # )

    generated_ids_trimmed = [
    out_ids[len(in_ids):]
    for in_ids, out_ids in zip(inputs["input_ids"], generated_ids)
    ]


    caption = processor.batch_decode(
        generated_ids,
        skip_special_tokens=True,
        clean_up_tokenization_spaces=False
    )[0].strip()

    parts = caption.rsplit("assistant", 1)
    if len(parts) == 2:
        caption = parts[1].strip()


    # print("=" * 80)
    # print(caption)
    # print("=" * 80)

    return caption