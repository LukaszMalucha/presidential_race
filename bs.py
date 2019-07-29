import bs4 as bs
from urllib.request import Request, urlopen
import urllib

req = urllib.request.Request(
    'https://www.oddschecker.com/politics/us-politics/us-presidential-election-2020/winner',
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)

f = urllib.request.urlopen(req)
soup = bs.BeautifulSoup(f, 'lxml')

table = soup.table

candidates = []
candidates_total = []
candidates_score = {}

for row in soup.find_all('tr', class_='diff-row evTabRow bc')[:15]:
    td = row.find_all('td')
    row = [i.text for i in td if len(i) > 0]
    candidates.append(row)

for row in candidates:
    row_split = []
    for element in row[1:]:
        element_1 = element.split('/')
        if len(element_1) == 1:
            element_1.append('1')
        row_split.append(element_1)
    candidates_total.append(row_split)
    final_score = 0
    for candidate in candidates_total:
        total_score = 0
        # print(candidate)
        for element in candidate:
            total = int(element[0]) / int(element[1])
            total_score += total

        final_score = total_score / len(candidate)
    print(final_score)
    candidates_score[row[0]] = final_score

print(candidates_score)

{'Donald Trump': 0.8894029581529582, 'Kamala Harris': 5.345833333333334, 'Elizabeth Warren': 7.264583333333333,
'Joe Biden': 7.325, 'Pete Buttigieg': 16.41904761904762, 'Bernie Sanders': 15.125, 'Andrew Yang': 29.391304347826086,
 'Tulsi Gabbard': 50.63478260869565, 'Mike Pence': 73.64999999999999, 'Cory Booker': 67.48333333333333, 'Beto ORourke': 68.49166666666666, 'Amy Klobuchar': 82.66666666666667,
 'Hillary Clinton': 107.5909090909091, 'Nikki Haley': 120.95833333333333, 'Julian Castro': 118.27272727272727}
