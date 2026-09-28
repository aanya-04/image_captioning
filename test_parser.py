from evaluation.parser import parse_response

response = """
Here are the rankings.

```json
[
    {
        "caption_id":1,
        "score":9.81,
        "rank":1,
        "reason":"Excellent."
    },
    {
        "caption_id":2,
        "score":9.42,
        "rank":2,
        "reason":"Missed background."
    }
]
"""