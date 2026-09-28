from evaluation.llava_evaluator import LlavaEvaluator

EXCEL_PATH = "outputs/captions.xlsx"

evaluator = LlavaEvaluator(EXCEL_PATH)
evaluator.evaluate()