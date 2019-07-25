import bs4 as bs
from urllib.request import Request, urlopen
import urllib
import requests

# sauce = urllib.request.urlopen("https://www.oddschecker.com/politics/us-politics/us-presidential-election-2020/winner", headers={'User-Agent': 'Mozilla/5.0'}).read()
# #
# soup = bs.BeautifulSoup(sauce,'lxml')

# sauce = Request('https://www.oddschecker.com/politics/us-politics/us-presidential-election-2020/winner', headers={'User-Agent': 'Mozilla/5.0'})
# soup = bs.BeautifulSoup(sauce,'lxml')


# print(soup)


# sauce = urllib.request.Request("https://www.oddschecker.com/politics/us-politics/us-presidential-election-2020/winner", headers={'User-Agent': 'Mozilla/5.0'})
# soup = bs.BeautifulSoup(sauce,'lxml')


req = urllib.request.Request(
    'https://www.oddschecker.com/politics/us-politics/us-presidential-election-2020/winner',
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)

f = urllib.request.urlopen(req)
# print(f.read().decode('utf-8'))
soup = bs.BeautifulSoup(f,'html')
print(soup)