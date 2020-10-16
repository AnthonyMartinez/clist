from bs4 import BeautifulSoup
from requests import get
import re
import pandas as pd

# TODO convert results -> dataframe checkout 10/14 - don't want to use beautiful soup, questioning whether any python
#  library is the move here, thinking of using puppeteer or at least selenium r = get(
#  "https://phoenix.craigslist.org/d/electronics/search/ela") r = r.text
with open('out.txt', 'r') as out:
    r = out.read()

# get pids
res = re.findall("<li class=\"result-row\" data-pid=\"([0-9]+)\"", r, re.MULTILINE)
print(res)
print(len(res))

# get prices
res = re.findall("<span class=\"result-price\">(.+)</span>", r, re.MULTILINE)[0::2]
print(res)
print(len(res))

# get titlj
# res = re.findall(r"<a.+data-id.|cas"
res = re.findall(r"<a.+data-id.+class=\"result-title hdrlnk\" id.+>(.+)</a>"
                 , r, re.MULTILINE)
print(res)
print(len(res))

