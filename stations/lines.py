from pprint import pprint

class Lines:
  def __init__(self, soup, color, ref): 
    self.soup = soup
    self.color = color
    self.ref = ref

    # points in points_dic are NOT ordered
    # they will be ordered by ways
    self.points_dict = self.get_points(self.soup)

    # need to get dic of ways
    self.ways_dict = self.get_ways(self.soup)
    
    # finally, relation, which has list of ways
    self.relation_list = self.get_relation(self.soup)
    
    # it's coming together
    self.ordered_points = self.get_order_points(self.relation_list, self.ways_dict, self.points_dict)  
  
  def get_points(self, soup) -> dict:
    # Gets ALL points in a dictionary
    # {ref: [lon, lat]}
    points_dict = {}

    for elem in soup.find_all('node'):
      id_ = elem.get('id')
      lon = elem.get('lon')
      lat = elem.get('lat')

      points_dict[id_] = [lon, lat]
    
    return points_dict
  
  def get_ways(self, soup) -> dict:
    ways_dict = {}

    for way in soup.find_all('way'):
      id_ = way.get('id')

      # only 1 child (<nd ref="...">)
      # each nd_ref is a point from points_doct
      children = way.findChildren('nd', recusrive=False)
      for tag in children:
        ref = tag.get('ref')

        try: ways_dict[id_].append(ref)
        except: ways_dict[id_] = [ref]
      
    return ways_dict

  def get_relation(self, soup) -> list:
    # <relation> has <member ref="...">
    # each member_ref is a way
    relation_members = []

    relation_elem = soup.find('relation')
    children = relation_elem.findChildren('member', recusrive=False)
    for member in children:
      # member type can be "node" => this is to oredr separate stations while we want to order the lines (a line of points)
      if member.get('type') == 'way':
        member_ref = member.get('ref')
        relation_members.append(member_ref)

    return relation_members
  
  def get_order_points(self, relation_members, ways_dict, points_dict) -> list:
    # need to order everything
    # relation has ways has points

    # NOTE: this needs to be a list of lists because the relation does not seem to give ways in order
    # so just keep them as separate lines because making them one LONG line causes incorrect connections
    ordered_points = []

    for member_ref in relation_members:
      # path is a list of refs of points
      path = ways_dict[member_ref]

      sub_line = []
      # this is one polyline
      # many of these make up the train line

      for point_ref in path:
        point = points_dict[point_ref]
        # ordered_points.append(point)

        sub_line.append(point)

      ordered_points.append(sub_line)

    return ordered_points

  def return_points(self):
    return {
      'ref': self.ref,
      'color': self.color,
      'points': self.ordered_points
    }  

