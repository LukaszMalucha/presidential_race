# import bs4 as bs
# from urllib.request import Request, urlopen
# import urllib
#
#
# req = urllib.request.Request(
#     'https://www.oddschecker.com/politics/us-politics/us-presidential-election-2020/winner',
#     data=None,
#     headers={
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
#     }
# )
#
# f = urllib.request.urlopen(req)
# soup = bs.BeautifulSoup(f,'lxml')
#
# table = soup.table
#
#
# table_rows = table.find_all('tr')
#
# # for tr in table_rows[1:2]:
# #     td = tr.find_all('td')
# #     row = [i.text for i in td]
# #     print(row)
#
#
# for row in soup.find_all('tr', class_='diff-row evTabRow bc')[1:2]:
#     td = row.find_all('td')
#     # td = td.replace('/', 'x')
#     row = [i.text for i in td]
#     for element in row:
#         element = element.replace('/', 'x')
#     print(row)
#

# kamala = ['Kamala Harris', '5', '11/2', '6', '9/2', '5', '9/2', '6', '9/2', '6', '6', '7', '6', '', '5', '11/2', '5', '5', '5', '5', '6', '5', '5', '', '5', '', '32/5', '21/5', '14/5', '32/5']
# del kamala[13]
# del kamala[22]
# del kamala[23]
# kamala_1 = []
# for element in kamala[1:]:
#     element_1 = element.split('/')
#     if len(element_1) == 1:
#         element_1.append('1')
#     kamala_1.append(element_1)
#
# print(kamala_1)


score = [['5', '1'], ['11', '2'], ['6', '1'], ['9', '2'], ['5', '1'], ['9', '2'], ['6', '1'], ['9', '2'], ['6', '1'], ['6', '1'], ['7', '1'], ['6', '1'], ['5', '1'], ['11', '2'], ['5', '1'], ['5', '1'], ['5', '1'], ['5', '1'], ['6', '1'], ['5', '1'], ['5', '1'], ['5', '1'], [
'32', '5'], ['21', '5'], ['14', '5'], ['32', '5']]

total_score = 0
for lst in score:
    total = int(lst[0]) / int(lst[1])

    total_score += total
    # total_score = total_score / len(score)



print (total_score / 26)














