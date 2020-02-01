import requests
from bs4 import BeautifulSoup
import json

from global_vars import LINES
from functions import Lines

data = []

for line in LINES:
  response = requests.get(f'https://api.openstreetmap.org/api/0.6/relation/{line["code"]}/full')
  if response.status_code == 200:
    
    soup = BeautifulSoup(response.content, "xml")
    print('got soup!')

    # sp = get_line(line['name'], line['ref'], line['color'], soup)
    # print(sp['name'])
    # data.append(sp)

    sp = Lines(soup, line['color'], line['ref'])
    data.append(sp.return_points())

# create file if not exists
f = open('src/data/lines.json', 'w')
with open('src/data/lines.json', 'w') as outfile: 
  json.dump(data, outfile)

print('Output')
