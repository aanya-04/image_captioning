from evaluation.excel_reader import ExcelReader

reader = ExcelReader("outputs/captions.xlsx")

groups = reader.get_groups()

print(f"\nTotal Images : {len(groups)}")

for image_name, captions in groups.items():

    print("\n" + "=" * 70)

    print(image_name)

    print(f"Captions : {len(captions)}")

    for item in captions:

        print(
            f"Row {item['row']} | "
            f"{item['prompt_name']} | "
            f"{item['inference_time']} sec"
        )