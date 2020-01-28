
def get_line(line_name, line_ref, color, soup):
  points = []
  stations = []

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
        'ref': ref
      })
    
    points.append({
      'id': id_
    })
  
  return {
    'name': line_name,
    'ref': line_ref,
    'color': color,
    'stations': stations,
    'points': points
  }
