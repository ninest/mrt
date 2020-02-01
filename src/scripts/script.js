import { mrtLine } from './functions.js'
import lines from './../data/lines.json'

mapboxgl.accessToken = 'pk.eyJ1IjoidGhlbWluZHN0b3JtIiwiYSI6ImNqemI5dTE4czAzM20zb3BsYzAzaDVrOXAifQ.SydstlfTME2vjERTmPo3XA';
var map = new mapboxgl.Map({
  container: 'map', // container id
  // style: 'mapbox://styles/mapbox/dark-v10', // stylesheet location
  style: 'mapbox://styles/themindstorm/ck5ui9vow1mei1inw89olbhs5/draft',
  center: [103.8, 1.351], // starting position [lng, lat]
  zoom: 11 // starting zoom
});

map.on('load', () => {

  map.addControl(
  new mapboxgl.GeolocateControl({
    positionOptions: {
      enableHighAccuracy: true
    },
      trackUserLocation: true
    })
  )

  map.addControl(new mapboxgl.NavigationControl());

  // console.log(lines)

  lines.forEach((line) => {
    // console.log(line.ref)
    // console.log(line.name)
    // console.log(line.color)

    line.points.forEach((sub_line, i) => {
      map.addLayer(mrtLine(
        line.ref + Math.random().toString(),
        sub_line,
        line.color
      ))
    })
  })


  // map.addLayer(mrtLine(
  //   'ref',
  //   [[lon, lat], ...],
  //   'color'
  // ))
})

