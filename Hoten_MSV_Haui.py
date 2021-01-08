import bs4 as bs
import urllib.request
import csv
__all__ = [bs, urllib.request, csv]

url = urllib.request.urlopen('https://sv.dhcnhn.vn/student/result/viewstudyresult?code=2019603611').read()

soup = bs.BeautifulSoup(url, 'lxml')
pages = soup.find_all('div', class_="k-panel-bwrap")
print(pages)
"""for i in range(2018600000, 2018610000):
    url = urllib.request.urlopen('https://sv.dhcnhn.vn/student/result/viewstudyresult?code='+str(i)).read()
    print(url)
    soup = bs.BeautifulSoup(url, 'lxml')
    pages = soup.find('table', class_="table table-bordered table-striped")
    print(pages)

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
            writer.writerow([titles,  links])"""
