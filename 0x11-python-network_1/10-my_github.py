#!/usr/bin/python3
"""Script that uses GitHub API to display your id"""
import requests
from sys import argv
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    auth = HTTPBasicAuth(username, password)

    try:
        r = requests.get("https://api.github.com/user", auth=auth)
        print(r.json()["id"])
    except Exception:
        print("None")
