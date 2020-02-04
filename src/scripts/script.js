import { mrtLine, stationNames } from './functions.js'
import lines from './../data/lines.json'

mapboxgl.accessToken = 'pk.eyJ1IjoidGhlbWluZHN0b3JtIiwiYSI6ImNqemI5dTE4czAzM20zb3BsYzAzaDVrOXAifQ.SydstlfTME2vjERTmPo3XA';
var map = new mapboxgl.Map({
  container: 'map',
  style: 'mapbox://styles/themindstorm/ck5ui9vow1mei1inw89olbhs5/draft',
  center: [103.8, 1.351], // starting position [lng, lat]
  zoom: 11 // starting zoom
});

map.on('load', () => {
  // add user location button
  map.addControl(new mapboxgl.GeolocateControl({
    positionOptions: {
      enableHighAccuracy: true
    }, trackUserLocation: true
  }))

  // add controls (+ and - button)
  map.addControl(new mapboxgl.NavigationControl());

  // add lines for each train line
  lines.forEach((line) => {
    line.points.forEach((sub_line, i) => {
      map.addLayer(mrtLine(
        line.ref + i.toString(),
        sub_line,
        line.color
      ))
    })
  })

  // add points to mark each train stations
  lines.forEach((line) => {
    var stationGeoJson = stationNames(line.stations)
    console.log(stationGeoJson)

    stationGeoJson.features.forEach((station) => {
      // create HTML elem
      var stationNameDisplay = document.createElement('div')
      stationNameDisplay.className = 'station-name'
      stationNameDisplay.innerHTML = `
        ${station.properties.description}
        <div class="spacer"></div>
      `

      var stationMarkerDisplay = document.createElement('div')
      stationMarkerDisplay.className = 'station-marker'
      stationMarkerDisplay.style.backgroundColor = line.color

      new mapboxgl.Marker(stationNameDisplay)
        .setLngLat(station.geometry.coordinates)
        .addTo(map)
      new mapboxgl.Marker(stationMarkerDisplay)
        .setLngLat(station.geometry.coordinates)
        .addTo(map)
    })
  })
})

map.on('zoom', () => {
  const currentZoom = map.getZoom()
  console.log(currentZoom)
})
