import requests
from bs4 import BeautifulSoup

URL = "https://www.olx.ua/d/uk/transport/legkovye-avtomobili/q-%D0%B0%D0%B2%D1%82%D0%BE-%D0%B4%D0%BB%D1%8F-%D0%B7%D1%81%D1%83/?utm_campaign=avto_dlya_zsu&utm_medium=virtual_category&utm_source=olx"

r = requests.get(URL)

data = r.text

soup = BeautifulSoup (data, 'html.parser')

# us = soup.find_all('a', {
#     "href":"/currencies/ethereum/markets/"
# })
#
#
#
# print(us[0].text)

ss = soup.find_all("h6")
print(ss)