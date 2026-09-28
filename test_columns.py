from openpyxl import load_workbook

from evaluation.columns import (
    get_column_map,
    get_column
)

EXCEL_PATH = "outputs/captions.xlsx"

workbook = load_workbook(EXCEL_PATH)

sheet = workbook.active

columns = get_column_map(sheet)

print("\nDetected Columns\n")

for name, number in columns.items():
    print(f"{number:>2}  ->  {name}")

print("\nCaption Column =", get_column(columns, "Caption"))