from models.qwen_loader import load_qwen_model

processor, model = load_qwen_model()

print()

print("Processor :", type(processor))
print("Model     :", type(model))
print("Device    :", model.device)