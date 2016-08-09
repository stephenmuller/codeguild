'use strict';

var plainStr = 'abcdefg';
var changeAmount = 12;

/**
* takes in a character, uses its utf-8 charaacter to move a uniform amount and
* returns it back shifter per the 'encrypytion key'
*/
function characterShift(letter, key) {
  var c = letter.charCodeAt(0);
  var returnValue = '';
  if (c >= 97 && c <= 122) {
    returnValue = String.fromCharCode((c - 97 + key) % 26 + 97);
  } else{
    returnValue = String.fromCharCode((c - 65 + key) % 26 + 65);
  }
  return returnValue;
}


/**
* Takes in a string and an amount to shift by, 'encryption key', converts it to
* an array, shifts each character by the specified amount, and repackages it as
* a string.
*/
function caesarEncrypt(toCaesarString, key) {
  var modifiedList = [];
  var output = '';
  var madeArray = toCaesarString.split();
  output += _.map(madeArray, characterShift(value, key));
  // can't get this to pass through the value
  output = modifiedList.join();
  return output;
}



var output = caesarEncrypt(plainStr, changeAmount);
console.dir(output);



/**
* Takes in a letter and the amount it's been shifted by and converts it back to
* the original character.
*/
function reverseShift(letter, key) {
  var c = letter.charCodeAt(0);
  var returnValue = '';
  if (c >= 97 && c <= 122) {
    returnValue = String.fromCharCode((c - 97 - key) % 26 + 97);
  } else{
    returnValue = String.fromCharCode((c - 65 - key) % 26 + 65);
  }
  return returnValue;
}


/**
* Takes in a string in its 'encrypyted' form, converts to an array, shifts back
* to the original characters and outputs it as a string.
*/
function decryptCaesar(caesarStr, key) {
  var modifiedList = [];
  var output = '';
  var madeArray = caesarStr.split();
  output += _.map(madeArray, reverseShift(value, key));
  // can't get this to pass through the value
  output = modifiedList.join();
  return output;
}


var outputTwo = decryptCaesar(output, changeAmount);

console.dir(outputTwo);
