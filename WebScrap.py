import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import numpy as np

URL = "https://stats.espncricinfo.com/ci/engine/records/averages/batting_bowling_by_team.html?id=13533;team=4345;type=tournament"
page = requests.get(URL)
bs = BeautifulSoup(page.content, 'lxml')

t_head = bs.find_all('thead')
for i, table in enumerate(t_head):
    rows = table.find_all('th')
    for row in rows:
        print(row.get('title'))
