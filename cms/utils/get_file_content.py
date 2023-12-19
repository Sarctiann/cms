""" ### This module contains functions for reading files programmatically.

Content:
--------
    - file_to_str(file_path) -> str
    - file_to_json(file_path) -> dict
"""

import json


def file_to_str(file_path) -> str:
    """Reads a file and returns the contents as a string."""
    with open(file_path, "r") as f:
        return f.read()


def file_to_json(file_path) -> dict:
    """Reads a file and returns the contents as a dict."""
    with open(file_path, "r") as f:
        return json.load(f)
