import urllib.request as urlreq
from bs4 import BeautifulSoup

# link = "https://codeforces.com/contest/177"

def contestPageParser( link ) :
    fp = urlreq.urlopen(link)
    html = fp.read().decode('utf-8')
    fp.close()

    problemcodes = []

    htmlObject = BeautifulSoup( html, 'html.parser' )
    
    for child in htmlObject.find_all('table'):
        if "class" in child.attrs.keys() and "problems" in child["class"] :
            for grandchild in child.descendants:
                try :
                    if grandchild.name == 'a' and "title" not in grandchild.attrs.keys() and grandchild.parent.name == 'td' :
                        problemcodes.append( grandchild.text.strip() )
                        # print( "-"*10)
                except :
                    continue

    return problemcodes
