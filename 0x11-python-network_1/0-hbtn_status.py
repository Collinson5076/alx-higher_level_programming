#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""

import urllib.request

"""Define the URL"""
url = "https://alx-intranet.hbtn.io/status"

"""Use a with statement to handle the request"""
with urllib.request.urlopen(url) as response:
    """Read the response content"""
    data = response.read()

    """Decode the content to a string"""
    decoded_data = data.decode('utf-8')

    """Print the response details"""
    print("Body response:")
    print(f"    - type: {type(data)}")
    print(f"    - content: {data}")
    print(f"    - utf8 content: {decoded_data}")
