import re

from bs4 import BeautifulSoup

import requests

link = 'https://www.mebelshara.ru/contacts'
response = requests.get(link).text
soup = BeautifulSoup(response, 'html.parser')
items = soup.find_all('div', {'class': 'city-item'})

city = str()
address = str()
latitude = str()
longitude = str()
store_name = str()
phone = str()
opening_hours = str()
work_days = str()
output_list = list()

for item in items:
    city = re.split('name">', str(item))[1].split('</h4>')[0]
    address = re.split('address="', str(item))[1].split('"')[0]
    latitude = re.split('latitude="', str(item))[1].split('"')[0]
    longitude = re.split('longitude="', str(item))[1].split('"')[0]
    store_name = re.split('shop-name">', str(item))[1].split('</')[0]
    opening_hours = re.split('mode2="', str(item))[1].split('"')[0]
    work_days = re.split('mode1="', str(item))[1].split('"')[0]
    phone = re.split('phone">', str(item))[1].split('</')[0]
    output_list.append({
        'address': f'{city}, {address}',
        'latlon': [latitude, longitude],
        'name': store_name,
        'phones': [phone],
        'working_hours': [work_days, opening_hours]})
for line in output_list:
    print(line)
