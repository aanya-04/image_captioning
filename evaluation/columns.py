"""
columns.py

Utility functions for handling Excel column mappings.

Instead of hardcoding column numbers, this module dynamically
reads the header row of the Excel sheet.
"""


def get_column_map(sheet):
    """
    Reads the first row of the worksheet and creates a mapping
    between column names and Excel column numbers.

    Example
    -------
    Excel:

    | Image | Category | Caption |

    Returns:

    {
        "Image": 1,
        "Category": 2,
        "Caption": 3
    }
    """

    column_map = {}

    for column in range(1, sheet.max_column + 1):

        header = sheet.cell(row=1, column=column).value

        if header is None:
            continue

        header = str(header).strip()

        if header != "":
            column_map[header] = column

    return column_map


def column_exists(column_map, column_name):
    """
    Returns True if a column exists.
    """

    return column_name in column_map


def get_column(column_map, column_name):
    """
    Safely returns the Excel column number.

    Raises an informative error if the column
    does not exist.
    """

    if column_name not in column_map:

        raise KeyError(
            f"Column '{column_name}' not found in Excel.\n"
            f"Available columns:\n{list(column_map.keys())}"
        )

    return column_map[column_name]