import requests
from bs4 import BeautifulSoup
import json

from global_vars import LINES
from lines import Lines
from stations import Stations

data = []

for line in LINES:
  response = requests.get(f'https://api.openstreetmap.org/api/0.6/relation/{line["code"]}/full')
  if response.status_code == 200:
    
    soup = BeautifulSoup(response.content, "xml")
    print('got soup!')

    points = Lines(soup, line['color'], line['ref'])
    stations = Stations(soup)

    data.append({
      **points.return_points(),
      **stations.return_stations()
    })

# create file if not exists
f = open('src/data/lines.json', 'w')
with open('src/data/lines.json', 'w') as outfile: 
  json.dump(data, outfile)

print('Output')
