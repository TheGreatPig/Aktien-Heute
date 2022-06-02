import csv
from numpy import full
import requests
import json
# plt.style.use('seaborn-whitegrid')



# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=TSLA&interval=15min&slice=year1month1&apikey=870B3E3WUK3MAU67'

with requests.Session() as s:
    download = s.get(CSV_URL)
    decoded_content = download.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    data = list(cr)

full_list = []
temporary_list = {}

for i in data:
    if i[1] != 'open':
        temporary_list['open'] = i[1]
        temporary_list['high'] = i[2]
        temporary_list['low'] = i[3]
        temporary_list['close'] = i[4]
        temporary_list['volume'] = i[5]
        print(temporary_list)
        full_list.append(temporary_list)
        temporary_list = {}


json_data = full_list


with open('../TSLA.json', 'w') as file:
    json.dump(json_data, file, indent=4)