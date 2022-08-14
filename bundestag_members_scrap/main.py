import requests
from bs4 import BeautifulSoup
import json
from time import sleep
import random

# persons_url_list = []
#
# print(f'Proceeding...')
#
# for i in range(0, 740, 20):
#     url = f'https://www.bundestag.de/ajax/filterlist/en/members/863330-863330?limit=20&noFilterSet=true&offset={i}'
#
#     req = requests.get(url)
#     request = req.content
#
#     soup = BeautifulSoup(request, 'lxml')
#     persons = soup.find_all('a')
#
#     for person in persons:
#         person_page_url = person.get('href')
#         if person_page_url:
#             persons_url_list.append(person_page_url)
#
#
# with open('persons_url_data.txt', 'a') as file:
#     for line in persons_url_list:
#         file.write(f'{line}\n')
#
# print(f'Finished')

with open('persons_url_data.txt') as file:
    lines = [line.strip() for line in file.readlines()]

    data_dict = []
    count = 0

    for line in lines:
        req = requests.get(line)
        request = req.content

        soup = BeautifulSoup(request, 'lxml')
        person = soup.find(class_='bt-biografie-name').find('h3').text
        person_name_party = person.strip().split(',')
        person_name = person_name_party[0]
        person_party = person_name_party[1].strip()

        social_networks = soup.find_all(class_='bt-link-extern')

        social_networks_url = []
        for item in social_networks:
            social_networks_url.append(item.get('href'))

        data = {
            'name': person_name,
            'political party': person_party,
            'social networks': social_networks_url
        }

        count += 1
        sleep(random.randrange(2, 6))
        print(f'№{count}: {line} is extracted')

        data_dict.append(data)

        with open('data.json', 'w') as json_file:
            json.dump(data_dict, json_file, indent=4)