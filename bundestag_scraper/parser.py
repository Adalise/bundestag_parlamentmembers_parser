COOLDOWN = 3 # seconds
INPUT_FILE = 'input.txt'
OUTPUT_FILE = 'output.json'

ABBREVATIONS = {
    'Bündnis 90/Die Grünen': 'B90',
    'Die Linke': 'LINKE',
    'CDU/CSU': 'CDU'
}

import bs4
import json
import time
import random
import requests

def get_deputies() -> list[str]:
    """Returns all deputies' codes (URLs without "https://www.bundestag.de/en/members/") as a list of strings"""

    with open(INPUT_FILE, 'r') as fp:
        return [line.strip() for line in fp.readlines()]

def get_deputy_data(deputy_code: str, abbreviate=False) -> dict:
    """Scrapes bundestag.de and parses the HTML.

    Args:
        deputy_code (str): URL suffix for the members page (e.g. scholz_olaf-860468)

    Returns:
        dict: Deputy details (name, party, social urls)
    """

    deputy_url = 'https://www.bundestag.de/en/members/' + deputy_code
    html_content = requests.get(deputy_url).content

    soup = bs4.BeautifulSoup(html_content, 'lxml')
    deputy_details = soup.find(class_='bt-biografie-name').find('h3').text.strip().split(',')

    deputy_name = deputy_details[0]
    deputy_party = deputy_details[1].strip()

    if abbreviate and deputy_party in ABBREVATIONS:
        deputy_party = ABBREVATIONS[deputy_party]

    social_media_urls = [item.get('href') for item in soup.find_all(class_='bt-link-extern')]

    deputy = {
        'name': deputy_name,
        'party': deputy_party,
        'social_media': social_media_urls
    }

    return deputy

def main():
    deputies = [] # Abgeordneter of the German Bundestag
    count = 0
    deputy_codes = get_deputies()
    number_deputies = len(deputy_codes)

    for deputy_code in deputy_codes:
        count += 1
        time.sleep(random.randrange(COOLDOWN-1, COOLDOWN+1))

        deputy = get_deputy_data(deputy_code, abbreviate=True)
        deputies.append(deputy)

        with open(OUTPUT_FILE, 'w') as fp:
            json.dump(deputies, fp, indent=4)

        print(f'{count}/{number_deputies} ({round((count / number_deputies) * 100, 1)}%) · {deputy["name"]} ({deputy["party"]})')

if __name__ == '__main__':
    main()