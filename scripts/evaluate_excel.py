from evaluation.evaluator import CaptionEvaluator

EXCEL_PATH = "outputs/captions.xlsx"

evaluator = CaptionEvaluator(EXCEL_PATH)

evaluator.evaluate()