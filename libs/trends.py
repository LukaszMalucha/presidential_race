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
springboard_scrape_path = os.path.join(my_path, "springboard_scrape.csv")


def data_extractor():
    """Dataset Extraction"""

    # Load WebPage
    source = requests.get('https://www.oddschecker.com/politics/us-politics/us-presidential-election-2020/winner').text

    # Pass source to beautifulsoup:
    soup = BeautifulSoup(source, 'lxml')

    # CSV file
    csv_file = open(springboard_scrape_path, 'w')

    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(
        ['title', 'add'])

    for candidate_div in soup.find_all('tr', class_="diff-row evTabRow bc"):

        try:
            name = candidate_div.find('div', class_="sel nm basket-active").text
            add = "asd"

        except Exception as e:

            name = None

        csv_writer.writerow(
            [name, add])

    csv_file.close()
