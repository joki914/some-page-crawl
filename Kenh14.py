import bs4 as bs
import urllib.request
__aLL__ = [bs, urllib.request]

url = urllib.request.urlopen("https://kenh14.vn/thi-vao-lop-10-nam-2020.html").read()
soup = bs.BeautifulSoup(url, 'lxml')

pages = soup.find_all('h3', class_='knswli-title')
times = soup.find_all('div', class_='knswli-meta')
contents = soup.find_all('span', class_='knswli-sapo')
f = open('kenh14.txt','w', encoding='utf8')

title = [page.find('a').attrs['title'] for page in pages]
link = [page.find('a').attrs['href'] for page in pages]
timePost = [time.find('span', class_='knswli-time').text for time in times]
contentPost = [content.text for content in contents]
for i in range(len(title)):
    print('Tiêu đề: {} '.format(title[i]))
    print('Thời gian: {} '.format(timePost[i]))
    print('Nội Dung: {} '.format(contentPost[i]))
    print('Link: kenh14.vn{}'.format(link[i]))
    print('----------------------------------------------------------')
    f.write('Tiêu đề: {} '.format(title[i]))
    f.write('\n')
    f.write('Thời gian: {} '.format(timePost[i]))
    f.write('\n')
    f.write('Nội Dung: {} '.format(contentPost[i]))
    f.write('\n')
    f.write('Link: kenh14.vn{}'.format(link[i]))
    f.write('\n')
    f.write('--------------------------------------------------------')
    f.write('\n')
f.close()


