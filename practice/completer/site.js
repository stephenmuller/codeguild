/**
* basic completer object, stores the list
*/
function Completer() {
    this.potentialCompletions = [];
}

/**
* completerProto is the prototype for the completer object, addCompletion adds
* a string to the array.
* removeCompletion removes a string from the array
* complete returns an array with matching instances of the given criteria
*/
var completerProto = {
  /**
  * Adds a string to the array in a Completer object
  */
  addCompletion: function(stringInput) {
    this.potentialCompletions.push(stringInput);
  },

  /**
  * Removes a string from the array in a Completer object
  */
  removeCompletion: function(stringInput) {
    _.pull(this.potentialCompletions, stringInput)
  },

  /**
  * uses the provided input to return a list of matches from the array
  */
  complete: function(prefix) {
    var toCheck = new RegExp(prefix)
    return _.filter(this.potentialCompletions, toCheck.test())
  }
};

Completer.prototype = completerProto;

//initialize new object
var wordList = new Completer();
// Generate some samples
wordList.addCompletion('banana')
wordList.addCompletion('boy')
wordList.addCompletion('apple')
wordList.addCompletion('vegetable')
//prove it works
console.dir(wordList)
//set up new RegExp
var testStr = '^b'
//run it
var testComplete = wordList.complete(testStr)
//prove it works
console.log(testComplete)
