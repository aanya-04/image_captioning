from evaluation.excel_reader import ExcelReader
from evaluation.prompts import build_prompt

reader = ExcelReader("outputs/captions.xlsx")

groups = reader.get_groups()

# Take the first image
image_name = list(groups.keys())[0]

captions = groups[image_name]

prompt = build_prompt(captions)

print("=" * 80)
print("IMAGE:", image_name)
print("=" * 80)
print(prompt)