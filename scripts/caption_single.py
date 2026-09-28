# from transformers import AutoProcessor, Qwen2_5_VLForConditionalGeneration
# from PIL import Image
# import torch
# import os
# import sys
# PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0, PROJECT_ROOT)

# from prompts.prompts import PROMPTS
# MODEL_NAME = "Qwen/Qwen2.5-VL-3B-Instruct"

# IMAGE_PATH = "images/cats/cat_003.jpg"

# PROMPT_NAME = "basic"

# DEVICE = "cuda" if torch.cuda.is_available() else "cpu"


# print("Loading model...")

# processor = AutoProcessor.from_pretrained(
#     MODEL_NAME,
#     trust_remote_code=True
# )

# model = Qwen2_5_VLForConditionalGeneration.from_pretrained(
#     MODEL_NAME,
#     torch_dtype=torch.float16 if DEVICE == "cuda" else torch.float32,
#     device_map="auto",
#     trust_remote_code=True,
# )

# print("Model loaded!")
# image = Image.open(IMAGE_PATH).convert("RGB")

# messages = [
#     {
#         "role": "user",
#         "content": [
#             {
#                 "type": "image",
#                 "image": image,
#             },
#             {
#                 "type": "text",
#                 "text": PROMPTS[PROMPT_NAME],
#             },
#         ],
#     }
# ]

# text = processor.apply_chat_template(
#     messages,
#     tokenize=False,
#     add_generation_prompt=True,
# )

# inputs = processor(
#     text=[text],
#     images=[image],
#     return_tensors="pt",
# )

# inputs = {k: v.to(model.device) for k, v in inputs.items()}


# with torch.no_grad():
#     generated_ids = model.generate(
#         **inputs,
#         max_new_tokens=512,
#         do_sample=False,
#         temperature=0.2,
#     )

# output = processor.batch_decode(
#     generated_ids,
#     skip_special_tokens=True,
#     clean_up_tokenization_spaces=True,
# )[0]

# print("\n" + "=" * 80)
# print("Prompt:", PROMPT_NAME)
# print("=" * 80)
# print(output)
# print("=" * 80)











import os
import sys
import gc
import torch

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from models.model_loader import load_model
from utils.preprocess import preprocess_image, check_image
from prompts.prompts import PROMPTS

IMAGE_PATH = os.path.join(
    PROJECT_ROOT,
    "images",
    "cats",
    "cat_003.jpg"
)

PROMPT_NAME = "basic"

check_image(IMAGE_PATH)

processor, model = load_model()

image = preprocess_image(IMAGE_PATH)

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
                "text": PROMPTS[PROMPT_NAME]
            }
        ]
    }
]

text = processor.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)

inputs = processor(
    text=[text],
    images=[image],
    return_tensors="pt"
)

inputs = {
    k: v.to(model.device)
    for k, v in inputs.items()
}

gc.collect()

if torch.cuda.is_available():
    torch.cuda.empty_cache()

with torch.no_grad():

    generated_ids = model.generate(
        **inputs,
        max_new_tokens=300,
        do_sample=False,
        use_cache=True,
    )

output = processor.batch_decode(
    generated_ids,
    skip_special_tokens=True,
    clean_up_tokenization_spaces=True
)[0]

print("\n" + "=" * 80)
print("Prompt :", PROMPT_NAME)
print("=" * 80)
print(output)
print("=" * 80)