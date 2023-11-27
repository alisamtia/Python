import urllib.request
import re
from re import findall


url="https://dev-umar17345.pantheonsite.io/index.php"

response=urllib.request.urlopen(url)
html=response.read()
htmlstring=html.decode()
getdata=findall("\d{10}",htmlstring)
for i in getdata:
    print(i)