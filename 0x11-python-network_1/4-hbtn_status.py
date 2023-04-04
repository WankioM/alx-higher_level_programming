#!/usr/bin/python3
"""Gets https://intranet.hbtn.io/status."""
import requests

url = 'https://alx-intranet.hbtn.io/status'

response = requests.get(url)

print('Body response:')
print('\t- type:', type(response.content))
print('\t- content:', response.content.decode())
