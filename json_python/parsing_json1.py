import urllib.request
import xml.etree.ElementTree as ET
import json

url = input('Enter location: ')
if len(url) < 1:
    url = 'https://py4e-data.dr-chuck.net/comments_2182078.json'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print(f'Retrieved {len(data)} characters')

num = list()

info = json.loads(data)
print("Count:", len(info['comments']))
for item in info['comments']:
    num.append(int(item['count']))
print('Sum:', sum(num))