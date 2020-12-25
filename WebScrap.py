import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import numpy as np


URL = "https://stats.espncricinfo.com/ci/engine/records/averages/batting_bowling_by_team.html?id=13533;team=4345;type=tournament"


def getIPLTeamStats(url):

    page = requests.get(URL)
    bs = BeautifulSoup(page.content, 'lxml')

    tables = bs.find_all('table', class_='engineTable')
    for table in tables:
        caption = table.find('caption')

        if caption != None:
            print(caption.text)

            if 'batting' in caption.text:
                captionText = caption.text
                endIndx = captionText.index('batting')
                print(captionText[:endIndx])
                th_list = table.find_all('th')
                for row in th_list:
                    print(row.get('title'))


getIPLTeamStats(URL)
