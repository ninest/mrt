
class Stations:
  def __init__(self, soup):
    self.soup = soup

    # get a dictionary of all stations
    # to be put in correct order later
    self.stations_dict = self.get_stations(self.soup)
    
    # get the order of the statins
    # this returns a list of refs (ids) which show the order of the stations
    self.relation_list = self.get_relation(self.soup)
    
    # it's coming together
    # using relation_list to order stations_dict
    self.ordered_points = self.get_ordered_stations(self.relation_list, self.stations_dict)
  
  def get_stations(self, soup) -> dict:
    # gets all stations UNORDERED
    stations_dict = {}

    for elem in soup.find_all('node'):
      id_ = elem.get('id')
      lon = elem.get('lon')
      lat = elem.get('lat')
      name = None  # if the name exists, we know it's a station
      ref = None  # ref may be None for some stations

      children = elem.findChildren('tag', recursive=False)
      for tag in children:
        if tag.get('k') == 'name':  name = tag.get('v')
        if tag.get('k') == 'ref':  ref = tag.get('v')
      
      # if the name is not None, it's a station
      if name:
        # the ref of an interchange should be split by ';'
        # should be in list form
        try: ref = ref.split(';')
        except: ref = [ref]

        stations_dict[id_] = {
          'name': name,
          'ref': ref,
          'lon': lon,
          'lat': lat
        }
    
    return stations_dict
  
  def get_relation(self, soup) -> list:
    # the <relation> tag has <member> children with role="stop"
    # this shows the order of the stations
    relation_members = []

    relation_elem = soup.find('relation')
    children = relation_elem.findChildren('member', recursive=False)
    for member in children:
      # need type="node" or role="stop"
      if member.get('type') == 'node':
        member_ref = member.get('ref')
        relation_members.append(member_ref)
    
    return relation_members
  
  def get_ordered_stations(self, relation_members, stations_dict) -> list:
    ordered_stations = []

    for member_ref in relation_members:
      try:
        ordered_stations.append(
          stations_dict[member_ref]
        )
      except:
        print("Issue in getting ordered stations.")
      
    
    return ordered_stations
  
  def return_stations(self) -> list:
    return {
      'stations': self.ordered_points
    }
