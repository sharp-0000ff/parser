import re

import json

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


def get_value(first_separator, item, second_separator):
    return re.split(first_separator, str(item))[1].split(second_separator)[0]


counter = 0
for item in items:
    counter = str(item).count('data-shop-address')
    if counter > 1:
        shops_same_city = re.split('shop-list-item', str(item))
        city = get_value('name">', item, '</h4>')
        for nested_item in shops_same_city:
            try:
                address = get_value('address="', nested_item, '"')
                latitude = get_value('latitude="', nested_item, '"')
                longitude = get_value('longitude="', nested_item, '"')
                store_name = get_value('shop-name">', nested_item, '</')
                opening_hours = get_value('mode2="', nested_item, '"')
                work_days = get_value('mode1="', nested_item, '"')
                phone = get_value('phone">', nested_item, '</')
                output_list.append({
                    'address': f'{city}, {address}',
                    'latlon': [latitude, longitude],
                    'name': store_name,
                    'phones': [phone],
                    'working_hours': [work_days, opening_hours]})
            except IndexError:
                # list index out of range (think about how to fix)
                pass
    else:
        city = get_value('name">', item, '</h4>')
        address = get_value('address="', item, '"')
        latitude = get_value('latitude="', item, '"')
        longitude = get_value('longitude="', item, '"')
        store_name = get_value('shop-name">', item, '</')
        opening_hours = get_value('mode2="', item, '"')
        work_days = get_value('mode1="', item, '"')
        phone = get_value('phone">', item, '</')
        output_list.append({
            'address': f'{city}, {address}',
            'latlon': [latitude, longitude],
            'name': store_name,
            'phones': phone,
            'working_hours': [work_days, opening_hours]})

with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(output_list, file, indent=4, ensure_ascii=False)
