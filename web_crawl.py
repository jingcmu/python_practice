import urlparse
import urllib
from bs4 import BeautifulSoup

url = "http://www.nytimes.com"

urls = [url] # stack of urls to scrape
visited = [url] # historic record of urls

while len(urls) > 0:
    try:
        htmltext = urllib.urlopen(urls[0]).read()
    except:
        print urls[0]

    soup = BeautifulSoup(htmltext)
    urls.pop(0);
    print len(urls)

    for tag in soup.findAll('a', href = True):
        tag['href'] = urlparse.urljoin(url, tag['href'])
        if url in tag['href'] and tag['href'] not in visited:
            urls.append(tag['href'])
            visited.append(tag['href'])
        if len(visited) == 1000:
            break

for tag in visited:
    print tag

