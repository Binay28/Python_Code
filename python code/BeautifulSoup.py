# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
count=int(input('Enter the count'))
position=int(input('Enter the position'))
url='http://py4e-data.dr-chuck.net/known_by_Judah.html'
while count>=0:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tag= soup('a')
    print(url)
    url=tag[position-1].get('href',None)
    #for tag in tags:
        #position=position-1
        #if position==0 :
            #print(tag.get('href', None))
            #url=tag.get('href',None)
        #print(tag.get('href', None))
    count=count-1   
