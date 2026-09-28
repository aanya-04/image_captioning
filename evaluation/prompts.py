# """
# prompts.py

# Prompt templates used for caption evaluation.

# The evaluator compares ALL captions for the SAME image and
# returns a relative ranking.
# """

# SYSTEM_PROMPT = """
# You are an expert in Computer Vision and Image Caption Evaluation.

# Your task is NOT to generate captions.

# Your task is to compare multiple captions describing the SAME image.

# Evaluate every caption based on:

# 1. Accuracy
#    - Does the caption correctly describe the image?
#    - Penalize incorrect objects, colors, breeds, counts, actions or relationships.

# 2. Detail
#    - Prefer captions that capture fine-grained visual details including:
#      - animal breed/species
#      - coat/fur color and markings
#      - pose
#      - facial expression
#      - eye contact
#      - background
#      - lighting
#      - objects
#      - camera angle
#      - environment

# 3. Completeness
#    - Reward captions that cover most visible information.

# 4. Hallucination
#    - Penalize any information that is not visible in the image.

# 5. Readability
#    - Prefer fluent, natural and well-structured captions.

# Scoring Guidelines

# 10.0 = Exceptional
# 9.0–9.9 = Excellent
# 8.0–8.9 = Very Good
# 7.0–7.9 = Good
# 6.0–6.9 = Acceptable
# Below 6 = Poor

# IMPORTANT

# Rank ALL captions relative to each other.

# Rank 1 must be the BEST caption.

# Do not assign duplicate ranks.

# Return ONLY valid JSON.

# Do NOT return markdown.

# Do NOT explain anything outside JSON.
# """


# USER_PROMPT_TEMPLATE = """
# Below is one image followed by multiple captions generated for that image.

# Compare every caption with every other caption.

# Rank them from BEST to WORST.

# For every caption provide:

# - score (0-10)
# - rank
# - reason 

# Captions

# {captions}

# # Return ONLY this JSON format.

# # [
# #     {{
# #         "caption_id": 1,
# #         "score": 9.82,
# #         "rank": 1,
# #         "reason": "Most accurate and detailed caption with no hallucinations."
# #     }},
# #     {{
# #         "caption_id": 2,
# #         "score": 9.37,
# #         "rank": 2,
# #         "reason": "Very detailed but missed some background information."
# #     }}
# # ]


# Return ONLY valid JSON.

# [
#     {{
#         "row": 15,
#         "score": 9.82,
#         "rank": 1,
#         "reason": "Most accurate and detailed caption."
#     }},
#     {{
#         "row": 16,
#         "score": 9.35,
#         "rank": 2,
#         "reason": "Very good but missed some background details."
#     }}
# ]
# """


# # def build_prompt(captions):
# #     """
# #     Build the evaluation prompt.

# #     Parameters
# #     ----------
# #     captions : list

# #     Example
# #     -------
# #     [
# #         {
# #             "row": 2,
# #             "caption": "...",
# #             ...
# #         },
# #         ...
# #     ]

# #     Returns
# #     -------
# #     str
# #         Prompt ready to send to the evaluation model.
# #     """

# #     caption_text = ""

# #     for idx, item in enumerate(captions, start=1):

# #         caption_text += (
# #             f"Caption {idx}\n"
# #             f"{item['caption']}\n\n"
# #         )

# #     return USER_PROMPT_TEMPLATE.format(
# #         captions=caption_text
# #     )


# def build_prompt(captions):
#     """
#     captions : list of dictionaries from ExcelReader
#     """

#     caption_text = ""

#     for item in captions:

#         caption_text += (
#             f"Row: {item['row']}\n"
#             f"Caption:\n"
#             f"{item['caption']}\n\n"
#         )

#     return USER_PROMPT_TEMPLATE.format(
#         captions=caption_text
#     )

















"""
prompts.py

Prompt templates used for caption evaluation.
The evaluator compares ALL captions for the SAME image and
returns a relative ranking.
"""

SYSTEM_PROMPT = """
You are an expert in Computer Vision, Vision-Language Models, and Image Caption Evaluation.

Your task is NOT to generate captions.

Your task is to evaluate and compare ONLY the captions provided for the SAME image.

Evaluation Criteria:

1. Accuracy
- Does the caption correctly describe the image?
- Penalize incorrect objects, colors, breeds, counts, actions, relationships or locations.

2. Detail
- Reward captions that include fine-grained visual details such as:
    • breed/species
    • fur or coat color
    • markings
    • pose
    • facial expression
    • eye direction
    • body posture
    • accessories
    • objects
    • lighting
    • shadows
    • background
    • environment
    • camera angle
    • framing
    • composition

3. Completeness
- Reward captions that describe most visible information.

4. Hallucination
- Penalize information that is not visible in the image.

5. Readability
- Prefer captions that are fluent, natural and well structured.

Scoring Scale

10.0 = Exceptional
9.0 - 9.9 = Excellent
8.0 - 8.9 = Very Good
7.0 - 7.9 = Good
6.0 - 6.9 = Acceptable
Below 6 = Poor

Rules

- Compare ONLY the captions provided.
- Never invent additional captions.
- Never invent additional row numbers.
- Return exactly one JSON object for every input caption.
- Use the EXACT row number provided.
- Rank all captions from BEST to WORST.
- Rank 1 = Best caption.
- Do not use duplicate ranks.
- Return ONLY valid JSON.
- Do NOT include markdown.
- Do NOT include explanations outside JSON.
"""

USER_PROMPT_TEMPLATE = """
One image is provided.

Below are {num_captions} captions generated for THIS SAME image.

Your job is to compare these captions against each other.

Caption List

{captions}

Instructions

Evaluate every caption using:

- Accuracy
- Visual Detail
- Completeness
- Hallucination
- Fluency

Then compute:

- Overall Score (0-10)
- Rank
- Short Reason

IMPORTANT

The number of JSON objects MUST equal {num_captions}.

Every input row must appear exactly once.

Do not create new rows.

Do not remove any rows.

Return ONLY valid JSON.

Required JSON schema:

[
    {{
        "row": integer,
        "score": number,
        "rank": integer,
        "reason": string
    }}
]
"""

def build_prompt(captions):
    """
    captions

    [
        {
            "row":2,
            "caption":"...."
        },
        ...
    ]
    """

    caption_text = ""

    for item in captions:

        caption_text += (
            f"Row: {item['row']}\n"
            f"Caption:\n"
            f"{item['caption']}\n\n"
        )

    # return USER_PROMPT_TEMPLATE.format(
    #     captions=caption_text,
    #     num_captions=len(captions)
    # )

    valid_rows = ", ".join(
         str(item["row"]) for item in captions
    )

    prompt = USER_PROMPT_TEMPLATE.format(
        captions=caption_text,
        num_captions=len(captions)
    )

    prompt += f"""

        IMPORTANT

        Valid Excel rows are ONLY:

        {valid_rows}

        Never return any row except those listed above.

        Never return row 1 because row 1 contains the Excel headers.
        """

    return prompt