import { mrtLine, stationNames, hideByClass, showByClass } from './functions.js'
import lines from './../data/lines.json'
import refs from './../data/refs.json'

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

  // don't want to write a station name twice
  // This happens to interchanges, so makeing a counter
  var stationsAdded = []

  // add points to mark each train stations
  lines.forEach((line) => {
    console.log(line)

    line.stations.forEach((station) => {
      let name = station.name
      // make sure labels are not doubled
      // adding dot and pill
      if (! stationsAdded.includes(name)) {
        stationsAdded.push(name)

        // create HTML elemnt for station name
        var stationNameDisplay = document.createElement('div')
        stationNameDisplay.className = 'station-name'
        stationNameDisplay.innerHTML = `
          ${name}
          <div class="spacer"></div>
        `
        new mapboxgl.Marker(stationNameDisplay)
        .setLngLat([station.lon, station.lat])
        .addTo(map)



        // HTML elem for station pill
        let refsForStation = refs.stations[name]
        var refsHTML = ``
        try {
          refsForStation.forEach((ref) => {
            let lineRef =  ref.substring(0,2).toLowerCase() // ew or ns ...
            console.log(lineRef)
            let color = refs.colors[lineRef]
            console.log(color)
            refsHTML += `<div class='ref' style="background-color: ${color}"> ${ref} </div>`
          })
        } catch {
          // TODO?
          console.log('Undefined Error ...')
        }

        var stationPill = document.createElement('div')
        stationPill.className = 'station-pill'
        stationPill.innerHTML = refsHTML

        new mapboxgl.Marker(stationPill)
          .setLngLat([station.lon, station.lat])
          .addTo(map)
      }

      // adding dot
      var stationMarkerDisplay = document.createElement('div')
      stationMarkerDisplay.className = 'station-marker'
      stationMarkerDisplay.style.backgroundColor = line.color

      new mapboxgl.Marker(stationMarkerDisplay)
        .setLngLat([station.lon, station.lat])
        .addTo(map)
    })
  })
})



function zoomChange() {
  // prevZoom
  const currentZoom = map.getZoom()
  console.log(currentZoom)

  // low zoom level: 
  // hide station names, pills with refs
  // only show dots
  if (currentZoom < 12) {
    hideByClass('station-name')
    hideByClass('station-pill')
    showByClass('station-marker')
  }

  // medium low zoom level
  // only show pill 
  if (currentZoom > 12) {
    showByClass('station-name')
    showByClass('station-pill')
    hideByClass('station-marker')
  }

  // high zoom level, show station names and pills
  // if 
}
map.on('zoom', zoomChange)
