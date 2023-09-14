#!/usr/bin/python3
"""define save to json file"""
import json


def save_to_json_file(my_obj, filename):
    """saves an object to a json file"""
    with open(filename, 'w') as thefile:
        json.dump(my_obj, thefile)
