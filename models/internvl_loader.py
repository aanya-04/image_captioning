"""
internvl_loader.py

Loads the InternVL3-2B model.
"""

import torch

from transformers import (
    AutoTokenizer,
    AutoModel
)

MODEL_NAME = "OpenGVLab/InternVL2_5-2B"

_tokenizer = None
_model = None


def load_internvl_model():

    global _tokenizer
    global _model

    if _tokenizer is not None and _model is not None:
        return _tokenizer, _model

    print("\nLoading InternVL Tokenizer...")

    _tokenizer = AutoTokenizer.from_pretrained(
        MODEL_NAME,
        trust_remote_code=True
    )

    print("Loading InternVL Model...")

    _model = AutoModel.from_pretrained(
        MODEL_NAME,
        trust_remote_code=True,
        torch_dtype=torch.float16,
        device_map="auto",
        low_cpu_mem_usage=True
    )

    _model.eval()

    print("InternVL Loaded Successfully!")

    return _tokenizer, _model