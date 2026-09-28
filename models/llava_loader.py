"""
llava_loader.py

Loads the LLaVA-1.5 model.
"""

import torch

from transformers import (
    AutoProcessor,
    LlavaForConditionalGeneration
)

MODEL_NAME = "llava-hf/llava-1.5-7b-hf"

_processor = None
_model = None


def load_llava_model():

    global _processor
    global _model

    if _processor is not None and _model is not None:
        return _processor, _model

    print("\nLoading LLaVA Processor...")

    _processor = AutoProcessor.from_pretrained(
        MODEL_NAME
    )

    print("Loading LLaVA Model...")

    _model = LlavaForConditionalGeneration.from_pretrained(
        MODEL_NAME,
        torch_dtype=torch.float16,
        device_map="auto"
    )

    _model.eval()

    print(" LLaVA Loaded Successfully!")

    return _processor, _model