import urllib.request # For parsing and downloading the html from a site.
from bs4 import BeautifulSoup

def parseURL( URL ):
    # The first part is getting thr HTML of the page.
    page = urllib.request.urlopen( URL )
    rawPageHTML = page.read()
    
    PageHTML = BeautifulSoup(rawPageHTML,'html5lib')
    
    ProblemStatement = PageHTML.find('div', attrs={'class':'problem-statement' })

    Input = PageHTML.find_all('pre')[0].string[:-1]
    # Ref : https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    Output = PageHTML.find_all('pre')[1].string[:-1]
    # The [:-1] is to remove the additonal line printed.
    print(Input)
    print(Output)
