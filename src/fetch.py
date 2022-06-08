from numpy import full
import requests
import json



URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=FB&interval=5min&apikey=870B3E3WUK3MAU67'

r = requests.get(URL)
data = r.json()

with open('backend/database/FB.json', 'w') as file:
    json.dump(data, file, indent=4)