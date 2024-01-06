#!/usr/bin/python3
"""Script that sends a request and displays the body of the response"""
from sys import argv
from urllib import request
from urllib.error import URLError


if __name__ == "__main__":
    try:
        req = request.Request(argv[1])
        with request.urlopen(req) as response:
            print(response.read().decode("utf-8"))
    except URLError as e:
        print("Error code: {}".format(e.code))
