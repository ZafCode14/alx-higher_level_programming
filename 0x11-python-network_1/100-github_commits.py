#!/usr/bin/python3
"""Script that solves the challange"""
import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get("https://api.github.com/repos/{}/{}/commits".format(argv[1], argv[2]))
    for i in range(10):
        print(r.json()[i].get("sha") + ":", r.json()[i].get("commit").get("author").get("name"))
