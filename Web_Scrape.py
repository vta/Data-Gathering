import requests
from bs4 import BeautifulSoup
url_to_scrape = 'http://data.vitalsigns.mtc.ca.gov/api/t5/flows/'
r = requests.get(url_to_scrape)
soup = BeautifulSoup(r.text)
print (soup.get_text())