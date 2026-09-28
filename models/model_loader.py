from transformers import (
    AutoProcessor,
    Qwen2_5_VLForConditionalGeneration,
)
import torch

MODEL_NAME = "Qwen/Qwen2.5-VL-3B-Instruct"

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

_processor = None
_model = None


def load_model():

    global _processor, _model

    if _processor is None:

        print("Loading processor...")

        _processor = AutoProcessor.from_pretrained(
            MODEL_NAME,
            trust_remote_code=True
        )
        # print(_processor.image_processor)

    if _model is None:

        print("Loading model...")

        _model = Qwen2_5_VLForConditionalGeneration.from_pretrained(
            MODEL_NAME,
            torch_dtype=torch.float16 if DEVICE == "cuda" else torch.float32,
            device_map="auto",
            trust_remote_code=True,
        )

        _model.eval()

        print("Model Loaded Successfully!")

    return _processor, _model