import requests
from bs4 import BeautifulSoup



URL = ("https://coinmarketcap.com/")

r = requests.get(URL)

data = r.text

print(data)
soup = BeautifulSoup (data, 'html.parser')


