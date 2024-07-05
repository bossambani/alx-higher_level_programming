#!/usr/bin/python3
# Python script that fetches https://alx-intranet.hbtn.io/status

if __name__ == "__main__":
    import urllib.request
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        data = response.read()
        print('Body response')
        print('\t - type:', type(data))
        print('\t - content:', data)
        print('\t - utf8 content:', data.decode('utf-8'))
