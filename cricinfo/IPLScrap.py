import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import numpy as np


class IPLTeamStat:

    def getIPLTeamStats(self, url):

        page = requests.get(url)
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
                    tr_list = table.find_all('tr', class_='data1')
                    # for row in th_list:
                    # print(row.get('title'))
                    for tr in tr_list:
                        td_list = tr.find_all('td')
                        for td in td_list:
                            print(td.text)
                if 'bowling' in caption.text:
                    captionText = caption.text
