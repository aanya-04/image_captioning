from models.llava_loader import load_llava_model

processor, model = load_llava_model()

print("\nProcessor Loaded :", type(processor))
print("Model Loaded     :", type(model))
print("\nEverything Loaded Successfully!")