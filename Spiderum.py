import bs4 as bs
import urllib.request
__aLL__ = [bs, urllib.request]

listLink = []
for llink in listLink:
    urlmain = urllib.request.urlopen(llink['Link']).read()
    soup = bs.BeautifulSoup(urlmain, 'lxml')
    getlinks = soup.find_all('a', class_='body')

    f = open('{}.txt'.format(llink['Name']), 'a', encoding='utf8')

    for link in getlinks:
        urlsub = urllib.request.urlopen('https://spiderum.com{}'.format(link.attrs['href'])).read()
        soupm = bs.BeautifulSoup(urlsub, 'lxml')
        titles = soupm.find('div', class_='post-main hide-content-noscript no-print')
        title = titles.find('div', class_='title')
        print(title.text)
        f.write('{}'.format(title.text))
        pages = soupm.find('div', class_='content')
        print(pages.text)
        f.write('{}'.format(pages.text))
        f.write('\n')

    f.close()
