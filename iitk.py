import urllib
from BeautifulSoup import BeautifulSoup
from re import search
import unicodedata

url = "https://in.yahoo.com/?p=us"
while True:
    #unicodedata.normalize('NFKD', tag.get('href')).encode('ascii','ignore')
    #print type(str(tag.get('href')))
    #if search('functions-of-doaa',str(tag.get('href'))) :
        #print "Opening Calendar..."
        #urllib.urlopen("file://"+str(tag.get('href')))
        #break
    handle = urllib.urlopen(url)
    html = handle.read()
    soup = BeautifulSoup(html)

    tags = soup.findAll('a')
    for tag in tags:
        print tag
    print "url :", url, "Length of tags:", len(tags)
    #f = str(tags[3].get('href'))
    #print "Fetching: ", f
    url = "https://in.yahoo.com/?p=us"#+f
    print url
