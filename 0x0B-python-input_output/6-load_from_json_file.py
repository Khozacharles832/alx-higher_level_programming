#!/usr/bin/python3
"""defines module 06"""
import json


def load_from_json_file(filename):
    """creates an object from a json file"""
    with open(filename, 'r') as the_file:
        return(json.load(the_file))
