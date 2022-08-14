# Bundestag Parlament Member Parser
Parses bundestag members:
- name
- political party
- social network URLs

## Details
Updated 14/08/22.

Problem with too many requests per second (and potential ratelimiting issues) solved by using random (but not too short) cooldowns between requests.

## Usage
### Windows, MacOS and GNU/Linux
```shell
git clone https://github.com/Adalise/bundestag_parlamentmembers_parser.git
cd bundestag_scraper

python parser.py
python analysis.py
```