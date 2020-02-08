import requests
import json

from global_vars import LINES

# stolen from another repo
# curl "Accept: application/json" -H "Content-Type: application/json" -H "Referer: http://journey.smrt.com.sg/journey/station_info/"  https://connect.smrt.wwprojects.com/smrt/api/stations/

station_dict = {}
# { 'station': ['ref1', 'ref2'] }
colors_dict = {}
for line in LINES:
  colors_dict[line['ref']] = line['color']

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json",
  "Referer": "http://journey.smrt.com.sg/journey/station_info/"
}
response = requests.get('https://connect.smrt.wwprojects.com/smrt/api/stations/', headers=headers)
if response.status_code == 200:
  content = json.loads(response.text)

  for station in content['results']:
    refs = station['code']
    if ',' in refs:
      refs = refs.split(',')
    else:
      refs = [refs]
    station_dict[station['name']] = refs
  
  print(station_dict)

  refs_dict = {
    'stations': station_dict,
    'colors': colors_dict
  }

  # create file if not exists
  f = open('src/data/refs.json', 'w')
  with open('src/data/refs.json', 'w') as outfile: 
    json.dump(refs_dict, outfile)

  print('Output')