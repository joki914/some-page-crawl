import urllib.request
import bs4 as bs
import requests
__all__ = [urllib.request, bs]
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url = requests.get('https://facbook.com/randy.bu.35/friends', verify=False).text
soup = bs.BeautifulSoup(url, 'lxml')

pages = soup.find_all('div', class_='fsl fwb fcb')
print(pages)
for page in pages:
    userName = page.find('a').attrs['href'].text()
    print(userName)

