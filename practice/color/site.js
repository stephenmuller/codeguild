// Make a Color type. Implement a Color(r, g, b) constructor where the values
// are between 0 and 255. Implement the following prototype methods:
//
// blend(other) that returns a new color half way between the two
// // toHex() that returns the CSS hex code of the color like #FF13C9

function Color(r, g, b) {
  this.r = r;
  this.g = g;
  this.b = b;
}

var colorProto = {
  blend: function (other) {
    var mergeRed = (this.r + other.r)/2;
    var mergeGreen = (this.g + other.g)/2;
    var mergeBlue = (this.b + other.b)/2;
    return new Color(
      Math.floor(mergeRed), Math.floor(mergeGreen), Math.floor(mergeBlue)
    )
  },

  toHex: function () {
    var hex = '0123456789ABCDEF';
    var output = ''
    var inputColor = [this.r, this.g, this.b]
    for (var i = 0; i < inputColor.length; i += 1) {
      var remainder = inputColor[i] % 16;
      hexValueOne = hex.charAt((inputColor[i] - remainder) / 16);
      hexValueTwo = hex.charAt(remainder)
      output += (hexValueOne + hexValueTwo)
    }
    return output
  }
};

Color.prototype = colorProto;

var red = new Color(255, 0, 0);
var green = new Color(0, 255, 0);
console.log(red.toHex());
console.log(red.blend(green));
