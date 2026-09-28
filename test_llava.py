from evaluation.llava_judge import LlavaJudge


judge = LlavaJudge()

captions = [
    {
        "row": 2,
        "caption": "A brown dog is standing on green grass looking toward the camera."
    }
]

results = judge.evaluate(
    image_path="images/dogs/dog_002.jpg",   # Change this if your image path is different
    captions=captions
)

print("\nFinal Results")
print(results)