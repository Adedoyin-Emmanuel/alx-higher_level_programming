#!/usr/bin/python3
"""This script adds all the arguments to a python list.
Then save the list to a file.
"""
import json
import sys
save_to_json = __import__("5-save_to_json_file").save_to_json_file
load_from_json = __import__("6-load_from_json_file").load_from_json_file


try:
    args = load_from_json("add-items.json")
except Exception:
    args = []
    args.extend(sys.argv[1:])
    save_to_json(args, "add-items.json")
