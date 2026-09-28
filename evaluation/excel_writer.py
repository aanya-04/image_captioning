"""
excel_writer.py

Writes evaluation results back into captions.xlsx.

Supports:
- Qwen
- LLaVA
- MiniCPM

Results are written into the existing rows.
"""

from openpyxl import load_workbook

from evaluation.columns import (
    get_column_map,
    get_column
)


class ExcelWriter:

    def __init__(self, excel_path):

        self.excel_path = excel_path

        self.workbook = load_workbook(excel_path)

        self.sheet = self.workbook.active

        self.columns = get_column_map(self.sheet)

    # ---------------------------------------------------
    # Generic Writer
    # ---------------------------------------------------

    def write_results(self, results, model_name):
        """
        Parameters
        ----------
        results : list

        Example

        [
            {
                "row": 2,
                "score": 9.8,
                "rank": 1,
                "reason": "Very accurate..."
            }
        ]

        model_name :
            "Qwen"
            "LLaVA"
            "MiniCPM"
        """

        score_col = get_column(
            self.columns,
            f"{model_name} Score"
        )

        rank_col = get_column(
            self.columns,
            f"{model_name} Rank"
        )

        reason_col = get_column(
            self.columns,
            f"{model_name} Reason"
        )

        for item in results:

            row = item["row"]

            self.sheet.cell(
                row=row,
                column=score_col
            ).value = item["score"]

            self.sheet.cell(
                row=row,
                column=rank_col
            ).value = item["rank"]

            self.sheet.cell(
                row=row,
                column=reason_col
            ).value = item["reason"]

    

    # def write_results(self, results, model_name):

    #     for item in results:

    #         row = item["row"]

    #         self.sheet.cell(row, self.QWEN_SCORE_COL).value = item["score"]

    #         self.sheet.cell(row, self.QWEN_RANK_COL).value = item["rank"]

    #         self.sheet.cell(row, self.QWEN_REASON_COL).value = item["reason"]

    



    # ---------------------------------------------------
    # Save
    # ---------------------------------------------------

    def save(self):

        self.workbook.save(self.excel_path)