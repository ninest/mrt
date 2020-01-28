import requests
from bs4 import BeautifulSoup

response = requests.get("https://api.openstreetmap.org/api/0.6/relation/445764/full")
if response.status_code == 200:

  soup = BeautifulSoup(response.content, "xml")

  points = []
  stations = []

  for elem in soup.find_all('node'):
    id_ = elem.get('id')
    lat = elem.get('lat')
    lon = elem.get('lon')

    print(id_)
    
    children = elem.findChildren('tag', recursive=False)
    for tag in children:
      # print(tag)
      if tag.get('k') == 'name':
        print(tag.get('v'))
      if tag.get('k') == 'ref':
        # some stations don't have the ref (?)
        print(tag.get('v'))

    print('-------------')

  # getting all points
  # points = []
  # for elem in tree:
  #   if 'lat' in elem.attrib and 'lon' in elem.attrib:
  #     points.append({
  #       'id': elem.attrib['id'],
  #       'lat': float(elem.attrib['lat']),
  #       'lon': float(elem.attrib['lon']),
  #     })
  
  # getting all stations
  # stations = []
  # for elem in tree:
  #   if len(elem):
  #     print(elem.attrib)
