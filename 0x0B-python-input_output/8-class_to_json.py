#!/usr/bin/python3
""" Returns the dict description of an obj """


def class_to_json(obj):
    return vars(obj)
