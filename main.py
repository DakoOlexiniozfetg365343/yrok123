import requests
from bs4 import BeautifulSoup

URL = "https://coinmarketcap.com/"

r = requests.get(URL)

data = r.text

soup = BeautifulSoup (data, 'html.parser')

us = soup.find_all('a', {
    "href":"/currencies/ethereum/markets/"
})



print(us[0].text)

