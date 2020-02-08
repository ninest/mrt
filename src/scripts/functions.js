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

export function stationNames(allStations) {
  // adds all station names for a line
  var stationPoints = {
    'type': 'FeatureCollection',
    'features': []
  }

  // https://docs.mapbox.com/mapbox-gl-js/example/variable-label-placement/
  allStations.forEach((station) => {
    // console.log(station)
    stationPoints.features.push({
      'type': 'Feature',
      'properties': {
        'description': station.name,
        // 'icon': 'circle-'
      },
      'geometry': {
        'type': 'Point',
        'coordinates': [station.lon, station.lat]
      }
    })
  })

  return stationPoints
}

export function hideByClass(className) {
  var hideDivs = document.getElementsByClassName(className)
  for (var i=0; i<hideDivs.length; i++) {
    hideDivs[i].style.display = 'none'
  }
}

export function showByClass(className) {
  var hideDivs = document.getElementsByClassName(className)
  for (var i=0; i<hideDivs.length; i++) {
    hideDivs[i].style.display = 'block'
  }
}