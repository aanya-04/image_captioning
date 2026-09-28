from PIL import Image
import os

MAX_SIZE = 1024


def preprocess_image(image_path):

    image = Image.open(image_path).convert("RGB")

    image.thumbnail((MAX_SIZE, MAX_SIZE))

    return image


def check_image(image_path):

    if not os.path.exists(image_path):
        raise FileNotFoundError(f"{image_path} does not exist.")

    return True