# import os
# import sys
# import pandas as pd

# PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0, PROJECT_ROOT)

# from models.model_loader import load_model
# from utils.caption_generator import generate_caption
# from prompts.prompts import PROMPTS

# processor, model = load_model()

# IMAGE_DIR = os.path.join(PROJECT_ROOT, "images")

# OUTPUT_DIR = os.path.join(PROJECT_ROOT, "outputs")
# os.makedirs(OUTPUT_DIR, exist_ok=True)

# results = []

# PROMPT_NAME = "basic"

# for category in ["cats", "dogs"]:

#     folder = os.path.join(IMAGE_DIR, category)

#     for image_name in sorted(os.listdir(folder)):

#         if not image_name.lower().endswith((".jpg", ".jpeg", ".png")):
#             continue

#         image_path = os.path.join(folder, image_name)

#         print(f"Processing {image_name}")

#         caption = generate_caption(
#             processor,
#             model,
#             image_path,
#             PROMPTS[PROMPT_NAME]
#         )

#         results.append({
#             "category": category,
#             "image_name": image_name,
#             "prompt_name": PROMPT_NAME,
#             "caption": caption
#         })

# df = pd.DataFrame(results)

# output_file = os.path.join(
#     OUTPUT_DIR,
#     "captions.csv"
# )

# df.to_csv(
#     output_file,
#     index=False
# )

# print("\nFinished!")
# print(df.head())




import os
import sys
import time


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)


from openpyxl import Workbook, load_workbook
from openpyxl.drawing.image import Image as XLImage
from monitoring.monitor import SystemMonitor
from models.model_loader import load_model
from utils.caption_generator import (generate_caption)
from prompts.prompts import PROMPTS


if len(sys.argv) != 3:
    print("Usage:")
    print("python scripts/caption_batch.py <start_index> <end_index>")
    sys.exit(1)

START_INDEX = int(sys.argv[1])
END_INDEX = int(sys.argv[2])


MODEL_NAME = "Qwen2.5-VL-3B-Instruct"

# PROMPT_NAME = "Detail"

IMAGE_DIR = os.path.join(PROJECT_ROOT, "images")

OUTPUT_DIR = os.path.join(PROJECT_ROOT, "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

OUTPUT_FILE = os.path.join(
    OUTPUT_DIR,
    "captions.xlsx"
)


if os.path.exists(OUTPUT_FILE):

    workbook = load_workbook(OUTPUT_FILE)
    sheet = workbook.active

else:

    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Captions"

    sheet.append([
        "Image",
        "Category",
        "Image Name",
        "Model",
        "Prompt Name",
        "Prompt",
        "Caption",
        "Inference Time (sec)",

        "TEMPERATURE",
        "TOP_P",
        
        "TOP_K",

        "Llava Score",
        "Llava Rank",
        "Llava Reason",

        # "MiniCPM Score",
        # "MiniCPM Rank",
        # "MiniCPM Reason",

        "MAX_TOKENS",

        "GPU Name",
        "Avg GPU Util (%)",
        "Peak GPU Util (%)",

        "Avg VRAM Used (MB)",
        "Peak VRAM Used (MB)",

        "GPU Temperature (°C)",

        "Avg CPU (%)",
        "Peak CPU (%)",

        "Avg RAM Used (GB)",
        "Peak RAM Used (GB)"
    ])

    sheet.column_dimensions["A"].width = 25
    sheet.column_dimensions["B"].width = 15
    sheet.column_dimensions["C"].width = 25
    sheet.column_dimensions["D"].width = 30
    sheet.column_dimensions["E"].width = 20
    sheet.column_dimensions["F"].width = 60
    sheet.column_dimensions["G"].width = 120
    sheet.column_dimensions["H"].width = 20

    sheet.column_dimensions["I"].width = 20
    sheet.column_dimensions["J"].width = 20
    sheet.column_dimensions["K"].width = 60
    sheet.column_dimensions["L"].width = 20
    sheet.column_dimensions["M"].width = 20
    sheet.column_dimensions["N"].width = 60
    # sheet.column_dimensions["O"].width = 20
    # sheet.column_dimensions["P"].width = 20
    # sheet.column_dimensions["Q"].width = 60



    sheet.column_dimensions["O"].width = 20
    sheet.column_dimensions["P"].width = 30
    sheet.column_dimensions["Q"].width = 18
    sheet.column_dimensions["R"].width = 18
    sheet.column_dimensions["S"].width = 18
    sheet.column_dimensions["T"].width = 18
    sheet.column_dimensions["U"].width = 18
    sheet.column_dimensions["V"].width = 18
    sheet.column_dimensions["W"].width = 18
    sheet.column_dimensions["X"].width = 18
    sheet.column_dimensions["Y"].width = 18


processor, model = load_model()
monitor = SystemMonitor(interval=0.5)

image_files = []

for category in ["cats"]:

        folder = os.path.join(IMAGE_DIR, category)

        for image_name in sorted(os.listdir(folder)):

            if image_name.lower().endswith((".jpg", ".jpeg", ".png")):

                image_files.append({
                    "category": category,
                    "image_name": image_name,
                    "image_path": os.path.join(folder, image_name)
                })

selected_images = image_files[START_INDEX:END_INDEX]

print(f"\nProcessing images {START_INDEX} to {END_INDEX-1}")
print(f"Total selected: {len(selected_images)}")
# caption generation

for idx, item in enumerate(selected_images, start=START_INDEX):

    category = item["category"]
    image_name = item["image_name"]
    image_path = item["image_path"]

    print(f"\n[{idx}] {image_name}")
    for prompt_name, prompt_text in PROMPTS.items():

        print(f"   Prompt : {prompt_name}")

        try:

            monitor.start()

            start = time.time()

            caption = generate_caption(
                processor,
                model,
                image_path,
                prompt_text
            )

            end = time.time()

        except Exception as e:

            monitor.stop()

            print(f"      Error : {e}")
            continue
        finally:

            monitor.stop()

        summary = monitor.summary()

        current_row = sheet.max_row + 1

            # Insert thumbnail
        excel_img = XLImage(image_path)
        excel_img.width = 120
        excel_img.height = 120

        sheet.add_image(excel_img, f"A{current_row}")
        sheet.row_dimensions[current_row].height = 95

            # Write data
        sheet.cell(current_row, 2).value = category
        sheet.cell(current_row, 3).value = image_name
        sheet.cell(current_row, 4).value = MODEL_NAME
        sheet.cell(current_row, 5).value = prompt_name
        sheet.cell(current_row, 6).value = prompt_text
        sheet.cell(current_row, 7).value = caption
        sheet.cell(current_row, 8).value = round(end - start, 2)

        sheet.cell(current_row, 9).value = 0.85
        sheet.cell(current_row, 10).value = 0.9
        sheet.cell(current_row, 11).value = None
        sheet.cell(current_row, 12).value = None
        sheet.cell(current_row, 13).value = None
        sheet.cell(current_row, 14).value = None
        # sheet.cell(current_row, 15).value = None
        # sheet.cell(current_row, 16).value = None
        # sheet.cell(current_row, 17).value = None

        sheet.cell(current_row, 15).value = 1200
        sheet.cell(current_row, 16).value = summary["GPU Name"]

        sheet.cell(current_row, 17).value = summary["Avg GPU Util (%)"]
        sheet.cell(current_row, 18).value = summary["Peak GPU Util (%)"]

        sheet.cell(current_row, 19).value = summary["Avg VRAM Used (MB)"]
        sheet.cell(current_row, 20).value = summary["Peak VRAM Used (MB)"]

        sheet.cell(current_row, 21).value = summary["Max GPU Temp (C)"]

        sheet.cell(current_row, 22).value = summary["Avg CPU (%)"]
        sheet.cell(current_row, 23).value = summary["Peak CPU (%)"]

        sheet.cell(current_row, 24).value = summary["Avg RAM Used (GB)"]
        sheet.cell(current_row, 25).value = summary["Peak RAM Used (GB)"]


        print("      Done")

        # except Exception as e:

        #     print(f"      Error : {e}")


# print("\nSaving Excel...")

# workbook.save(OUTPUT_FILE)

# print("\n")
# print("Finished Successfully!")
# print(f"Excel saved at:\n{OUTPUT_FILE}")
# # print("")
try:
    workbook.save(OUTPUT_FILE)
    print("saved")
except PermissionError:
    print(
        "Could not save the Excel file. "
        "Please close it if it's open in Excel/LibreOffice and try again."
    )

