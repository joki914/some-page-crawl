import bs4 as bs
import urllib.request

__all__ = [bs, urllib.request]

url = urllib.request.urlopen("http://index-of.es/Attacks/").read()
soup = bs.BeautifulSoup(url, 'lxml')
print(soup)
pages = soup.find_all('a')

#for page
#print(lin)