
        

from evaluation.excel_reader import ExcelReader
from evaluation.excel_writer import ExcelWriter
from evaluation.qwen_judge import QwenJudge
from evaluation.llava_judge import LlavaJudge


class CaptionEvaluator:

    def __init__(self, excel_path):

        self.reader = ExcelReader(excel_path)
        self.writer = ExcelWriter(excel_path)

        self.qwen = QwenJudge()
        self.llava = LlavaJudge()

    def evaluate(self):

        groups = self.reader.get_groups()

        print(f"\nFound {len(groups)} images.\n")

        for image_name, captions in groups.items():

            print("=" * 80)
            print(image_name)
            print("=" * 80)

            image_path = captions[0]["image_path"]

            print(f"Evaluating {len(captions)} captions...")

            # ---------------------------
            # Qwen
            # ---------------------------

            qwen_results = self.qwen.evaluate(
                image_path=image_path,
                captions=captions
            )

            self.writer.write_results(
                qwen_results,
                "Qwen"
            )

            # ---------------------------
            # LLaVA
            # ---------------------------

            llava_results = self.llava.evaluate(
                image_path=image_path,
                captions=captions
            )

            self.writer.write_results(
                llava_results,
                "Llava"
            )

            print("Done\n")

        self.writer.save()

        print("Evaluation Finished!")