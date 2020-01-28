import requests
from bs4 import BeautifulSoup

from global_vars import LINES
# TODO ^

from functions import get_line

response = requests.get("https://api.openstreetmap.org/api/0.6/relation/445764/full")
if response.status_code == 200:

  soup = BeautifulSoup(response.content, "xml")

  sp = get_line('east-west', 'ew', '00ff00', soup)
  print(sp)
  