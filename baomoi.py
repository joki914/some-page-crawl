import bs4 as bs
import urllib.request
import csv
__all__ = [bs, urllib.request]

url = urllib.request.urlopen('https://baomoi.com').read()
soup = bs.BeautifulSoup(url, 'lxml')
pages = soup.find_all('h4', class_='story__heading')
for page in pages:
    titles = page.find('a').attrs['title']
    links = page.find('a').attrs['href']
    print('Title: {} | Links: baomoi.com{}'.format(titles,links))

with open('Baomoi.csv', 'w', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Title', 'Link'])

    for page in pages:
        titles = page.find('a').attrs['title']
        links = 'baomoi.com'+page.find('a').attrs['href']
        writer.writerow([titles, links])
