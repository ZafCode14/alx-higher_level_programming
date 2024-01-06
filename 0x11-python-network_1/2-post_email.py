#!/usr/bin/python3
"""This module sends a POST request and displays the body of the response"""
from sys import argv
from urllib import request
from urllib import parse


if __name__ == "__main__":
    url = argv[1]
    values = {"email": argv[2]}

    data = parse.urlencode(values)
    data = data.encode("ascii")
    req = request.Request(url, data)

    with request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
