import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import numpy as np
from cricinfo import IPLScrap

URL = "https://stats.espncricinfo.com/ci/engine/records/averages/batting_bowling_by_team.html?id=13533;team=4345;type=tournament"

iplWebscrap = IPLScrap.IPLTeamStat()
iplWebscrap.getIPLTeamStats(URL)
