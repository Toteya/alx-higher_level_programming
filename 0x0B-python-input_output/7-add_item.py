#!/usr/bin/python3
""" Module 7-add_item """
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_file.json"
try:
    a_list = load_from_json_file(filename)
except FileNotFoundError:
    a_list = []

a_list.extend(sys.argv[1:])
save_to_json_file(a_list, filename)
