import urllib.request, urllib.parse, urllib.error
import json

url = 'http://py4e-data.dr-chuck.net/comments_75974.json'

sum=0

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
jsdata = json.loads(data)

cmts= jsdata["comments"]

for c in cmts:
    print(c['name'], c['count'])
    sum=sum+int(c['count'])

print(sum)