'use strict';

console.log(latLon)

var map;
function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: {
      lat: latLon.lat,
      lng: latLon.lon
    },
    zoom: 8
  })
};
