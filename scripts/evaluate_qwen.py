from evaluation.qwen_evaluator import QwenEvaluator

EXCEL_PATH = "outputs/captions.xlsx"

evaluator = QwenEvaluator(EXCEL_PATH)
evaluator.evaluate()