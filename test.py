import urllib.request as urlreq
from bs4 import BeautifulSoup

link = "https://codeforces.com/problemset/problem/1705/A"

fp = urlreq.urlopen(link)

html = fp.read().decode('utf-8')

fp.close()

htmlObject = BeautifulSoup(html, 'html.parser')

print(htmlObject)