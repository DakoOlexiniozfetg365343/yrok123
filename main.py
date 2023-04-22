import requests
from bs4 import BeautifulSoup
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

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

for n in ss:
    print(n.text)



uri = "mongodb+srv://sashadakopro:1234@dakota.unewuos.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")

    db = client["Alexij"]
    collection = db['Items']


    for n in ss:
        print(n.text)
        collection.insert_one({"item": n.text})

except Exception as e:
    print(e)

