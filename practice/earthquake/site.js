'use strict';
/**
* appease linter gods
*/
if (!ol) {
  var ol;
}

/**
* generates the style element for dots on the fly so that they can be individually
* scaled based on magnitude
*/
function generateStyle(feature) {
  return new ol.style.Style({
    image: new ol.style.Circle({
      radius: Math.abs(feature.get('mag') * 2),
      fill: new ol.style.Fill({color: 'rgba(255, 0, 0, 0.3)'}),
      stroke: new ol.style.Stroke({color: '#bada55', width: 1})
    })
  });
}

/**
* makes a new feature
*/
function makeFeature(item) {
  var coord = ol.proj.fromLonLat([item.geometry.coordinates[0],
    item.geometry.coordinates[1]]);
  return new ol.Feature({
    'geometry': new ol.geom.Point(coord),
    'size': 10000,
    'mag': item.properties.mag
  });
}

/**
*
*/
function generateFeatures(data) {
  return _.map(data.features, makeFeature);
}

/**
* generates the points on the map and puts them in place
*/
function renderMap(data) {
  var features = generateFeatures(data);
  var vectorSource = new ol.source.Vector({features: features});
  var vector = new ol.layer.Vector({
    source: vectorSource,
    style: generateStyle
  });
  var map = new ol.Map({
    target: document.getElementById('map'),
    layers: [new ol.layer.Tile({source: new ol.source.OSM()}), vector],
    view: new ol.View({
      center: [0, 0],
      zoom: 2
    })
  });
}



/**
*Requests a weeks worth of earthquake data
*/
function getEarthquakes() {
  var url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson';
  var data =  Promise.resolve($.ajax({
    dataType: 'json',
    url: url,
  }));
  return data;
}

function main() {
  getEarthquakes().then(renderMap);
}


$(document).ready(main);
