import csv
import requests
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')



# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=TSLA&interval=15min&slice=year1month1&apikey=870B3E3WUK3MAU67'

with requests.Session() as s:
    download = s.get(CSV_URL)
    decoded_content = download.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    data = list(cr)

    x_coordinates = []
    y_coordinates = []

    for y in data:
        y_coordinates.append(y[1])
        print(y)
        
    
    x_coordinates = range(0,len(y_coordinates))
    
    plt.plot(x_coordinates, y_coordinates, color = 'black')

    x_coordinates, y_coordinates = [], []

    for y in data:
        y_coordinates.append(y[2])

    x_coordinates = range(0,len(y_coordinates))

    plt.plot(x_coordinates, y_coordinates, color = 'blue')

    x_coordinates, y_coordinates = [], []

    for y in data:
        y_coordinates.append(y[3])

    x_coordinates = range(0,len(y_coordinates))

    plt.plot(x_coordinates, y_coordinates, color = 'green')

    x_coordinates, y_coordinates = [], []

    for y in data:
        y_coordinates.append(y[4])

    x_coordinates = range(0,len(y_coordinates))

    plt.plot(x_coordinates, y_coordinates, color = 'yellow')

    x_coordinates, y_coordinates = [], []

    for y in data:
        y_coordinates.append(y[5])

    x_coordinates = range(0,len(y_coordinates))

    plt.plot(x_coordinates, y_coordinates, color = 'red')

    x_coordinates, y_coordinates = [], []

    plt.show()