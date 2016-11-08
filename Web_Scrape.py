import requests
from bs4 import BeautifulSoup
import pandas as pd
url_to_scrape = 'http://data.vitalsigns.mtc.ca.gov/api/t5/flows/'
r = requests.get(url_to_scrape)
pd.DataFrame(r.json())
