export function mrtLine(id, coords, color) {
  return {
    'id': id,
    'type': 'line',
    'source': {
      'type': 'geojson',
      'data': {
        'type': 'Feature',
        'properties': {},
        'geometry': {
          'type': 'LineString',
          'coordinates': coords
        }
      }
    },
    'layout': {
      'line-join': 'round',
      'line-cap': 'round',
    },
    'paint': {
      'line-color': color,
      'line-width': 3,
      'line-opacity': 0.6
    }
  }
}