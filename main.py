import re

from bs4 import BeautifulSoup

import requests


link = 'https://www.mebelshara.ru/contacts'
response = requests.get(link).text
soup = BeautifulSoup(response, 'html.parser')
items = soup.find_all('div', {'class': 'city-item'})
print(items)
