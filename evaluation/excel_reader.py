# """
# excel_reader.py

# Reads the captions Excel file and groups all captions
# belonging to the same image.

# This module never modifies the Excel.
# """

# from collections import defaultdict
# from openpyxl import load_workbook

# from evaluation.columns import (
#     get_column_map,
#     get_column
# )


# class ExcelReader:

#     def __init__(self, excel_path, image_root="images"):

#         self.excel_path = excel_path
#         self.image_root = image_root

#         self.workbook = load_workbook(excel_path)

#         self.sheet = self.workbook.active

#         self.columns = get_column_map(self.sheet)

#     def get_groups(self):
#         """
#         Groups all rows by Image Name.

#         Returns
#         -------
#         {
#             "dog_001.jpg": [
#                 {
#                     "row": 2,
#                     "image": "...",
#                     "category": "...",
#                     "model": "...",
#                     "prompt_name": "...",
#                     "prompt": "...",
#                     "caption": "...",
#                     "inference_time": ...
#                 },
#                 ...
#             ]
#         }
#         """

#         groups = defaultdict(list)

#         for row in range(2, self.sheet.max_row + 1):

#             image_name = self.sheet.cell(
#                 row,
#                 get_column(self.columns, "Image Name")
#             ).value

#             if image_name is None:
#                 continue

#             item = {

#                 "row": row,

#                 "image_name": image_name,

#                 "category": self.sheet.cell(
#                     row,
#                     get_column(self.columns, "Category")
#                 ).value,

#                 "image_path ": os.path.join(
#                     self.image_root,
#                     category,
#                     image_name
#                 ),

#                 "model": self.sheet.cell(
#                     row,
#                     get_column(self.columns, "Model")
#                 ).value,

#                 "prompt_name": self.sheet.cell(
#                     row,
#                     get_column(self.columns, "Prompt Name")
#                 ).value,

#                 "prompt": self.sheet.cell(
#                     row,
#                     get_column(self.columns, "Prompt")
#                 ).value,

#                 "caption": self.sheet.cell(
#                     row,
#                     get_column(self.columns, "Caption")
#                 ).value,

#                 "inference_time": self.sheet.cell(
#                     row,
#                     get_column(self.columns, "Inference Time (sec)")
#                 ).value
#             }

#             groups[image_name].append(item)

#         return dict(groups)

#     def get_sheet(self):
#         return self.sheet

#     def get_workbook(self):
#         return self.workbook












"""
excel_reader.py

Reads the captions Excel file and groups all captions
belonging to the same image.
"""

import os
from collections import defaultdict
from openpyxl import load_workbook

from evaluation.columns import (
    get_column_map,
    get_column
)


class ExcelReader:

    def __init__(self, excel_path, image_root="images"):

        self.excel_path = excel_path
        self.image_root = image_root

        self.workbook = load_workbook(excel_path)
        self.sheet = self.workbook.active

        self.columns = get_column_map(self.sheet)

    def get_groups(self):

        groups = defaultdict(list)

        for row in range(2, self.sheet.max_row + 1):

            image_name = self.sheet.cell(
                row,
                get_column(self.columns, "Image Name")
            ).value

            if image_name is None:
                continue

            category = self.sheet.cell(
                row,
                get_column(self.columns, "Category")
            ).value

            image_path = os.path.join(
                self.image_root,
                category,
                image_name
            )

            item = {

                "row": row,

                "image_name": image_name,

                "image_path": image_path,

                "category": category,

                "model": self.sheet.cell(
                    row,
                    get_column(self.columns, "Model")
                ).value,

                "prompt_name": self.sheet.cell(
                    row,
                    get_column(self.columns, "Prompt Name")
                ).value,

                "prompt": self.sheet.cell(
                    row,
                    get_column(self.columns, "Prompt")
                ).value,

                "caption": self.sheet.cell(
                    row,
                    get_column(self.columns, "Caption")
                ).value,

                "inference_time": self.sheet.cell(
                    row,
                    get_column(self.columns, "Inference Time (sec)")
                ).value
            }

            groups[image_name].append(item)

        return dict(groups)

    def get_sheet(self):
        return self.sheet

    def get_workbook(self):
        return self.workbook