import bs4 as bs
import urllib.request
import csv
__all__ = [bs, urllib.request, csv]


url = urllib.request.urlopen('https://vnexpress.net/').read()
soup = bs.BeautifulSoup(url, 'lxml')
pages = soup.find_all('p', class_="description")
#panel panel-default panel-border-color panel-border-color-primary
for page in pages:
    titles = page.find('a').attrs['title']
    links = page.find('a').attrs['href']
    print('Title: {} - Link: {}'.format(titles, links))

with open('Vnexpress.csv', 'w', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Title', 'Link'])

    for page in pages:
        titles = page.find('a').attrs['title']
        links = page.find('a').attrs['href']
        writer.writerow([titles,  links])
