#!/usr/bin/python3
""" Returns python data structure in json format """


import json


def from_json_string(my_str):
    """The from json string method."""
    return json.loads(my_str)
