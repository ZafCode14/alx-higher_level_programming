#!/usr/bin/python3
"""Script that sends a requesnt to the URL and displays
the value of the X-Request-Id"""
from sys import argv
from urllib import request


if __name__ == "__main__":
    req = request.Request(argv[1])
    with request.urlopen(req) as response:
        print(response.headers["X-Request-Id"])
