import bs4 as bs
from urllib.request import Request
import urllib
import datetime
from operator import itemgetter
from http.client import IncompleteRead

candidates_set = {'Donald Trump', 'Kamala Harris', 'Elizabeth Warren', 'Joe Biden', 'Bernie Sanders', 'Pete Buttigieg',
                  'Andrew Yang', 'Tulsi Gabbard', 'Cory Booker', 'Beto ORourke', 'Julian Castro', 'Amy Klobuchar',
                  'Hillary Clinton'}


def get_data():
    try:
        req = urllib.request.Request(
            'https://www.oddschecker.com/politics/us-politics/us-presidential-election-2020/winner',
            data=None,
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
            })
    except IncompleteRead:
        req = urllib.request.Request(
            'https://www.oddschecker.com/politics/us-politics/us-presidential-election-2020/winner',
            data=None,
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
            })

    f = urllib.request.urlopen(req)
    soup = bs.BeautifulSoup(f, 'lxml')

    candidates = []
    candidates_total = []
    candidates_score = []
    date = str(datetime.date.today())

    # get candidates
    for row in soup.find_all('tr', class_='diff-row evTabRow bc')[:20]:
        td = row.find_all('td')
        row = [i.text for i in td if len(i) > 0]
        candidates.append(row)

    # prepare data for each candidate
    for row in candidates:
        row_split = []
        if row[0] in candidates_set:
            first_name = row[0].split(' ')[0]
            surname = row[0].split(' ')[1]
            image = row[0].replace(' ', '-') + '.jpg'
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
                score_rounded = round(final_score, 0)
                cash_prize = 100 + score_rounded * 100

            candidates_score.append((first_name, surname, cash_prize, image))
    max_prize = max(map(lambda x: x[2], candidates_score))
    candidates_score.insert(0, ('date', date, 0))

    candidates_score = sorted(candidates_score, key=itemgetter(2))

    return candidates_score, max_prize
