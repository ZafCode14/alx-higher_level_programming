#!/usr/bin/python3
"""Script that solves the challange"""
import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get(
            "https://api.github.com/repos/{}/{}/commits".format(
                argv[2], argv[1]))
    commit = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commit[i].get("sha"),
                commit[i].get("commit").get("author").get("name")))
    except Exception:
        pass
