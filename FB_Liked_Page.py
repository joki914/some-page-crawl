import bs4 as bs
import urllib.request
import csv

__all__ = [bs, urllib.request, csv]

fbid = input('Nhập FB ID(UserName): ')
urlfb = 'https://facebook.com/{}/likes'.format(fbid)
print(urlfb)
url = urllib.request.urlopen(urlfb)
soup = bs.BeautifulSoup(url, 'lxml')
print(soup)