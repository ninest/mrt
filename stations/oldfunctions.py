
def get_line(line_name, line_ref, color, soup):
  stations = []

  # contains refs from <way>
  way_refs = []

  # contains refs from members in relation
  member_refs = []

  unordered_points = get_dict_points(soup)
  
  # sort based on id
  for way in soup.find_all('way'):
    id_ = way.get('id')
    children = way.findChildren('nd', recursive=False)
    for tag in children:
      ref = tag.get('ref')
      way_refs.append(ref)

  ordered_points = []
  for ref in way_refs:
    ordered_points.append(points[ref])

  print(ordered_points)
  return {
    'name': line_name,
    'ref': line_ref,
    'color': color,
    'stations': stations,
    # 'points': points
    'points': ordered_points
  }


def get_dict_points(soup):
  points = {}
  for elem in soup.find_all('node'):
    id_ = elem.get('id')
    lat = elem.get('lat')
    lon = elem.get('lon')

    name = None
    # initializing because ref can be empty
    ref = ''
    
    children = elem.findChildren('tag', recursive=False)
    for tag in children:
      if tag.get('k') == 'name':
        name = tag.get('v')
      if tag.get('k') == 'ref':
        # some stations don't have the ref (?)
        ref = tag.get('v')

    if name:
      stations.append({
        'id': id_,
        'name': name,
        'ref': ref,
        'lat': lat,
        'lon': lon
      })
    
    points[id_] = [lon, lat]
  
  return points

