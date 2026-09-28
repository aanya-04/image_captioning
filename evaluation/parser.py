"""
parser.py

Parses the output returned by the evaluation models.

It extracts the JSON list and converts it into
Python dictionaries.
"""

import json
import re


def parse_response(response):
    """
    Parameters
    ----------
    response : str

    Raw output returned by Qwen/LLaVA/MiniCPM.

    Returns
    -------
    list

    Example

    [
        {
            "caption_id": 1,
            "score": 9.81,
            "rank": 1,
            "reason": "Most accurate."
        }
    ]
    """

    if not response:

        raise ValueError("Empty response received.")

    # ----------------------------------------
    # Remove markdown fences
    # ----------------------------------------

    response = response.replace("```json", "")
    response = response.replace("```", "")

    response = response.strip()

    # ----------------------------------------
    # Extract JSON array
    # ----------------------------------------

    match = re.search(r"\[.*\]", response, re.DOTALL)

    if match is None:

        raise ValueError(
            "Could not find JSON array in response."
        )

    json_text = match.group()

    # ----------------------------------------
    # Parse JSON
    # ----------------------------------------

    try:

        data = json.loads(json_text)

    except json.JSONDecodeError as e:

        raise ValueError(
            f"Invalid JSON returned.\n{e}"
        )

    # ----------------------------------------
    # Validation
    # ----------------------------------------

    if not isinstance(data, list):

        raise ValueError(
            "Expected a JSON list."
        )

    required = {

        "row",

        "score",

        "rank",

        "reason"

    }

    for item in data:

        missing = required - set(item.keys())

        if missing:

            raise ValueError(

                f"Missing fields: {missing}"

            )

    return data