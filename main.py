import re

from bs4 import BeautifulSoup

import requests

link = 'https://www.mebelshara.ru/contacts'
response = requests.get(link).text
soup = BeautifulSoup(response, 'html.parser')
items = soup.find_all('div', {'class': 'city-item'})

output_list = list()
city = str()
address = str()
latitude = str()
longitude = str()
store_name = str()
phone = str()
opening_hours = str()
work_days = str()


def get_value(first_separator, second_separator):
    return re.split(first_separator, str(item))[1].split(second_separator)[0]


for item in items:
    city = get_value('name">', '</h4>')
    address = get_value('address="', '"')
    latitude = get_value('latitude="', '"')
    longitude = get_value('longitude="', '"')
    store_name = get_value('shop-name">', '</')
    opening_hours = get_value('mode2="', '"')
    work_days = get_value('mode1="', '"')
    phone = get_value('phone">', '</')
    output_list.append({
        'address': f'{city}, {address}',
        'latlon': [latitude, longitude],
        'name': store_name,
        'phones': [phone],
        'working_hours': [work_days, opening_hours]})

for line in output_list:
    print(line)
