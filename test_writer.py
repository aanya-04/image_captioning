from evaluation.excel_writer import ExcelWriter

writer = ExcelWriter("outputs/captions.xlsx")

dummy_results = [

    {
        "row":2,
        "score":9.8,
        "rank":1,
        "reason":"Excellent caption."
    },

    {
        "row":3,
        "score":8.9,
        "rank":2,
        "reason":"Missed lighting."
    }

]

writer.write_results(
    dummy_results,
    "Qwen"
)

writer.save()

print("Done")