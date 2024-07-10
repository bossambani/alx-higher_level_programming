#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""
import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print('Error code: ', e.code)
    except urllib.error.URLError as e:
        print('Failed to reach the server:', e.reason)
