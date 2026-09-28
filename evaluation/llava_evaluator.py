from evaluation.excel_reader import ExcelReader
from evaluation.excel_writer import ExcelWriter
from evaluation.llava_judge import LlavaJudge


class LlavaEvaluator:

    def __init__(self, excel_path):

        self.reader = ExcelReader(excel_path)
        self.writer = ExcelWriter(excel_path)

        self.llava = LlavaJudge()

    def evaluate(self):

        groups = self.reader.get_groups()

        print(f"\nFound {len(groups)} images.\n")

        for image_name, captions in groups.items():

            print("=" * 80)
            print(image_name)
            print("=" * 80)

            image_path = captions[0]["image_path"]

            results = self.llava.evaluate(
                image_path=image_path,
                captions=captions
            )

            self.writer.write_results(
                results,
                "Llava"
            )

            print("Done\n")

        self.writer.save()

        print("LLaVA Evaluation Finished!")