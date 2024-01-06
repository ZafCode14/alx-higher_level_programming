#!/usr/bin/python3
"""Script that sends a POST request with a letter as a parameter"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) == 1:
        letter = ""
    else:
        letter = argv[1]
    try:
        r = requests.post(
                "http://0.0.0.0:5000/search_user", data={"q": letter})
        if r.json() == {}:
            print("No result")
        else:
            print("[{}] {}".format(r.json()["id"], r.json()["name"]))
    except Exception:
        print("Not a valid JOSN")
