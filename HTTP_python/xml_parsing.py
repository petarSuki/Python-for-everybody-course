import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter location: ')
if len(url) < 1:
    url = 'https://py4e-data.dr-chuck.net/comments_2182077.xml'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)

counts = tree.findall('.//count')
num = list()
for result in counts:
    # Debug print the data 
    print(result.text)
    num.append(int(result.text))

print('Count:', len(num))
print('Sum:', sum(num))
