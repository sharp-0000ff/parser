import re

from bs4 import BeautifulSoup

import requests


link = 'https://www.mebelshara.ru/contacts'
response = requests.get(link)
print(response.text)
