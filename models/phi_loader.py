"""
phi_loader.py

Loads Phi-3.5 Vision.
"""

import torch

from transformers import (
    AutoProcessor,
    AutoModelForCausalLM
)

MODEL_NAME = "microsoft/Phi-3.5-vision-instruct"

_processor = None
_model = None


def load_phi_model():

    global _processor
    global _model

    if _processor is not None and _model is not None:
        return _processor, _model

    print("\nLoading Phi Processor...")

    _processor = AutoProcessor.from_pretrained(
        MODEL_NAME,
        trust_remote_code=True
    )

    print("Loading Phi Model...")

    _model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        trust_remote_code=True,
        torch_dtype=torch.float16,
        device_map="auto"
    )

    _model.eval()

    print("✅ Phi Loaded Successfully!")

    return _processor, _model