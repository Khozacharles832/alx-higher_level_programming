#!/usr/bin/python3
""" load from json file """

import json


def load_from_json_file(filename):
    """loads data to a .json file."""
    with open(filename, "r", encoding="UTF-8") as f:
        return json.load(f)
