#!/usr/bin/python3
"""defines module 07"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_to_json_file = __import__('6-load_from_json_file.py').load_from_json_file


try:
    my_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    my_list = []
for i in range(1, len(sys.argv)):
    my_list.append(sys.arv[i])
save_to_json_file(my_list, "add_item.json")
