import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
import os.path
from django.conf import settings
from bs4 import BeautifulSoup
import requests
import datetime
import nltk
import csv

my_path = os.path.abspath(os.path.dirname(__file__))
springboard_scrape_path = os.path.join(settings.BASE_DIR, "springboard_scrape.csv")
springboard_clean_path = os.path.join(settings.BASE_DIR, "data/datasets/springboard_clean.csv")
springboard_mlb_path = os.path.join(settings.BASE_DIR, "data/datasets/springboard_mlb.csv")
stopwords_path = os.path.join(settings.BASE_DIR, "data/datasets/stopwords.txt")

def data_extractor():
    """Dataset Extraction"""

    # Load WebPage
    source = requests.get('https://trends.google.com/trends/explore?date=now%207-d&geo=US&q=tulsi%20gabbard,donald%20trump,cory%20booker,elizabeth%20warren,Pete%20Buttgieg').text

    # Pass source to beautifulsoup:
    soup = BeautifulSoup(source, 'lxml')

    # CSV file
    csv_file = open(springboard_scrape_path, 'w')

    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(
        ['title', 'provider', 'award', 'ects_credits', 'mode', 'deadline', 'start_date', 'end_date', 'nfq', 'ote_flag',
         'skill_area', 'link'])

    for candidate_div in soup.find_all('div', class_="grid outright-item"):

        try:
            # Course Title
            name = candidate_div.find('div', class_="panel-heading").h3.text

            # First Content Row

            fodds = candidate_div.find('div', class_="panel-body")

            # Provider:
            provider = first_row.find('div', class_="col-md-12").p
            provider = str(provider).split('</strong>')[1]
            provider = provider.split('<')[0]

            # Award:
            award = first_row.find('div', class_="col-md-5").p
            award = str(award).split('</strong>')[1]
            award = award.split('<')[0]

            # ECTS credits:
            credits = first_row.find('div', class_="col-md-3")
            credits = str(credits).split('</strong> ')[1]
            credits = credits.split('<')[0]

            # Second Content Row

            second_row = first_row.find_all('div', "row")[2]

            # Mode:
            mode = second_row.find('div', class_="col-md-5")
            mode = str(mode).split('</strong> ')[1]
            mode = mode.split('<')[0]

            # Application Deadline:
            deadline = second_row.find('div', class_="col-md-4")
            deadline = str(deadline).split('</strong>')[1]
            deadline = deadline.split('<')[0]

            # Start Date
            start_date = second_row.find('div', class_="col-md-3")
            start_date = str(start_date).split('</strong>')[1]
            start_date = start_date.split('<')[0]

            # End Date
            end_date = second_row.find('div', class_="col-md-3")
            end_date = str(end_date).split('</strong>')[2]
            end_date = end_date.replace(" ", "")
            end_date = end_date.split('<')[0]

            # Bottom Content Row

            third_row = first_row.find('div', "row margin-bottom-0")

            # NFQ
            nfq = third_row.find('div', class_="col-md-5").p
            nfq = str(nfq).split('</strong>')[1]
            nfq = nfq.split('<')[0]

            # Open to those in employment
            ote_flag = third_row.find('div', class_="col-md-4").p
            ote_flag = str(ote_flag).split('</strong>')[1]
            ote_flag = ote_flag.split('<')[0]

            # Skills area
            skill_list = third_row.find('div', class_="col-md-3")
            skill_list = str(skill_list).split('</strong>')[1]
            skill_list = skill_list.split('<')[0]
            skill_list = my_tokenizer(skill_list)

            # Course Link
            link = course_div.find('a')
            link = link.get('href')

        except Exception as e:

            title_div = None
            provider = None
            award = None
            credits = None
            mode = None
            deadline = None
            start_date = None
            end_date = None
            nfq = None
            ote_flag = None
            skill_list = None
            link = None

        csv_writer.writerow(
            [title_div, provider, award, credits, mode, deadline, start_date, end_date, nfq, ote_flag, skill_list,
             link])

    csv_file.close()