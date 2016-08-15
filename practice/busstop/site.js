'use strict';

function getBusRoutes(loc) {
  var newLoc = loc.join(',');
  console.log(newLoc);
  var PARAMS = {
    'll': newLoc, 'meters': 300, 'json': true, 'appID': superSecretTrimetKey,
    'showRoutes': true
  };
  var url = 'http://developer.trimet.org/ws/V1/stops';
  return Promise.resolve($.ajax({
    dataType: 'json',
    url: url,
    data: PARAMS
  }));
}


function printRouteList(position) {
  var location  = [position.coords.latitude, position.coords.longitude];
  getBusRoutes(location).
    then(function(responseObjectFromJSON) {
      var rtNumbers = getRouteNumbers(responseObjectFromJSON);
      _.forEach(rtNumbers, putRtLinkOnPage);
    });
}


function linkGenerator(rtNumber) {
  var strRtNumber = rtNumber.toString();
  if (strRtNumber.length === 2) {
    strRtNumber = '0' + strRtNumber;
  }
  return 'http://trimet.org/schedules/r' + strRtNumber + '.htm';
}

function getRouteNumbers(JSONObject) {
  var locations = JSONObject.resultSet.location;
  var mappedRouteArray = _.flatMap(locations, function(location) {
    return location.route;
  });
  var routeNumberArray = _.map(mappedRouteArray, function(mappedRouteArray) {
    return mappedRouteArray.route;
  });
  return _.uniq(routeNumberArray);
}


function putRtLinkOnPage(rtNumber) {
  var busItem = $('<li></li>');
  var rtNumberAsString =  rtNumber.toString();
  var busLink = $('<a>' + rtNumberAsString + '</a>');
  var link = linkGenerator(rtNumber);
  busLink.attr('href', link);
  busItem.append(busLink);
  $('#buses').append(busItem);
}

function main() {
  navigator.geolocation.getCurrentPosition(printRouteList);
}

$(document).ready(main);
