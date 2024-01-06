#!/usr/bin/python3
"""Module with a python script that fetches url"""
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        data = response.read()

    print("Body resopnse:")
    print("    - type: {}".format(type(data)))
    print("    - content: {}".format(data))
    print("    - utf8 content: {}".format(data.decode('utf-8')))
