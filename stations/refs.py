import requests
import json

# stolen from another repo
# curl "Accept: application/json" -H "Content-Type: application/json" -H "Referer: http://journey.smrt.com.sg/journey/station_info/"  https://connect.smrt.wwprojects.com/smrt/api/stations/

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json",
  "Referer": "http://journey.smrt.com.sg/journey/station_info/"
}
response = requests.get('https://connect.smrt.wwprojects.com/smrt/api/stations/', headers=headers)
if response.status_code == 200:
  content = json.loads(response.text)

  station_dict = {}
  # { 'station': ['ref1', 'ref2'] }

  for station in content['results']:
    refs = station['code']
    if ',' in refs:
      refs = refs.split(',')
    else:
      refs = [refs]
    station_dict[station['name']] = refs
  
  print(station_dict)

  # create file if not exists
  f = open('src/data/refs.json', 'w')
  with open('src/data/refs.json', 'w') as outfile: 
    json.dump(station_dict, outfile)

  print('Output')