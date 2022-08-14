import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.bundestag.de/en/members/abdi_sanae-861028')
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

print(f'Name: {person_name}\n'
      f'Political Party: {person_party}')

for item in social_networks_url:
    print(item)