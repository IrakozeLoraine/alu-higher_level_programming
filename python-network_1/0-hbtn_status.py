#!/usr/bin/python3
"""A script that
- fetches http://0.0.0.0:5050/status.
- uses urlib package
"""
import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen('http://0.0.0.0:5050/status') as res:
        content = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
