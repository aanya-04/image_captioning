# import os
# import requests
# from tqdm import tqdm

# # ==============================
# # CONFIGURATION
# # ==============================

# API_KEY = "oVKHlJTvxOly7rexXOu56DCTt5FsdUs85f5Lw3AOuFLA6aZViN0lwkhh"

# HEADERS = {
#     "Authorization": API_KEY
# }

# OUTPUT_DIR = "../images"

# DOWNLOADS = {
#     "cat": 50,
#     "dog": 50
# }

# PER_PAGE = 80

# MIN_WIDTH = 2048
# MIN_HEIGHT = 2048

# # ==============================
# # CREATE OUTPUT FOLDERS
# # ==============================

# for category in DOWNLOADS:
#     os.makedirs(os.path.join(OUTPUT_DIR, category + "s"), exist_ok=True)


# def download_images(query, total_images):

#     save_folder = os.path.join(OUTPUT_DIR, query + "s")

#     downloaded = 0
#     page = 1

#     while downloaded < total_images:

#         url = (
#             f"https://api.pexels.com/v1/search"
#             f"?query={query}"
#             f"&per_page={PER_PAGE}"
#             f"&page={page}"
#         )

#         response = requests.get(url, headers=HEADERS)

#         if response.status_code != 200:
#             print(response.text)
#             break

#         photos = response.json()["photos"]

#         if not photos:
#             break

#         for photo in tqdm(photos, desc=f"{query} page {page}"):

#             if downloaded >= total_images:
#                 break

#             width = photo["width"]
#             height = photo["height"]

#             # Skip images smaller than 2048 x 2048
#             if width < MIN_WIDTH or height < MIN_HEIGHT:
#                 continue

#             image_url = photo["src"]["original"]

#             filename = os.path.join(
#                 save_folder,
#                 f"{query}_{downloaded+1:03d}.jpg"
#             )

#             try:
#                 img = requests.get(image_url, timeout=30)

#                 with open(filename, "wb") as f:
#                     f.write(img.content)

#                 downloaded += 1

#             except Exception as e:
#                 print(e)

#         page += 1

#     print(f"{query}: {downloaded} images downloaded.")


# if __name__ == "__main__":

#     for category, count in DOWNLOADS.items():
#         download_images(category, count)

#     print("Finished!") 






import os
import requests
from tqdm import tqdm

# =====================================================
# CONFIGURATION
# =====================================================

API_KEY = "YOUR_PEXELS_API_KEY"  # <-- Replace with your API key

HEADERS = {
    "Authorization": API_KEY
}

# Number of images to download
DOWNLOADS = {
    "cat": 50,
    "dog": 50
}

PER_PAGE = 80

MIN_WIDTH = 2048
MIN_HEIGHT = 2048

# =====================================================
# PROJECT PATHS
# =====================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE_DIR, "images")

print(f"Images will be saved in: {OUTPUT_DIR}")

# Create folders
for category in DOWNLOADS:
    os.makedirs(os.path.join(OUTPUT_DIR, category + "s"), exist_ok=True)


# =====================================================
# DOWNLOAD FUNCTION
# =====================================================

def download_images(query, total_images):

    save_folder = os.path.join(OUTPUT_DIR, query + "s")

    downloaded = 0
    page = 1

    while downloaded < total_images:

        print(f"\nFetching page {page} for {query}s...")

        url = (
            f"https://api.pexels.com/v1/search"
            f"?query={query}"
            f"&per_page={PER_PAGE}"
            f"&page={page}"
        )

        response = requests.get(url, headers=HEADERS)

        if response.status_code != 200:
            print("API Error:", response.status_code)
            print(response.text)
            return

        photos = response.json().get("photos", [])

        if not photos:
            print("No more photos found.")
            break

        for photo in tqdm(photos):

            if downloaded >= total_images:
                break

            width = photo["width"]
            height = photo["height"]

            if width < MIN_WIDTH or height < MIN_HEIGHT:
                continue

            image_url = photo["src"]["original"]

            filename = os.path.join(
                save_folder,
                f"{query}_{downloaded+1:03d}.jpg"
            )

            try:

                img = requests.get(image_url, timeout=30)

                if img.status_code != 200:
                    print(f"Failed: {img.status_code}")
                    continue

                with open(filename, "wb") as f:
                    f.write(img.content)

                downloaded += 1

            except Exception as e:
                print(e)

        page += 1

    print(f"{query}: Downloaded {downloaded} images")


# =====================================================
# MAIN
# =====================================================

if __name__ == "__main__":

    for category, count in DOWNLOADS.items():
        download_images(category, count)

    print("\nFinished!")