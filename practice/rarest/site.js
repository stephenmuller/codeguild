"use strict";
function main(){
var namesToAges = {
    "Alyssa": 22,
    "Charley": 25,
    "Dan": 25,
    "Jeff": 20,
    "Kasey": 20,
    "Kim": 20,
    "Morgan": 25,
    "Ryan": 25,
    "Stef": 22
};

var ageList = []

for (var key in namesToAges) {
    var value = namesToAges[key];

    ageList.push(value);
}
console.dir(ageList)

var grouped = _.groupBy(namesToAges, Math.floor)
var mapped = _.mapValues(grouped, function(x) {
  return x.length;
});

var output =  _.minBy(_.keys(mapped), function(o) {
  return mapped[o];
 });

console.log('grouped')
console.dir(grouped)
console.log('mapped')
console.dir(temp)
console.log('output')
console.dir(output)
}

main();
