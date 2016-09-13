'use strict';


/**
* makes a field background green
*/
function setValid(fieldToSet) {
  $(fieldToSet).removeClass('invalid').addClass('valid');
}


/**
* makes a field background yellow
*/
function setInvalid(fieldToSet) {
  $(fieldToSet).removeClass('valid').addClass('invalid');
}

/**
* tests an input box vs the regexp
*/
function testValue(fieldToTest, regExpTest) {
  return regExpTest.test(fieldToTest.val());
}

/**
*test and set output
*/
function setFieldBackground(fieldPointer, testKey) {
  if (testValue(fieldPointer, testKey)) {
    setValid(fieldPointer);
  } else {
    setInvalid(fieldPointer);
  }
}

/**
* handles birthdate field validation
*/
function birthdateHandler() {
  var regexpTest = /\d{4}\-\d{2}\-\d{2}/;
  var toTest = $('#birth-date');
  setFieldBackground(toTest, regexpTest);
}

/**
*handles name field validation
*/
function nameHandler() {
  // insures that the name field has at least one character for first/last and a space
  var regexpTest = /^[a-z]+\s[a-z]+$/i;
  // sets ID for the field to pass along
  var toTest = $('#full-name');
  setFieldBackground(toTest, regexpTest);
}

/**
* handles phone# field validation
*/
function phoneNumberHandler() {
  var regexpTest = /^\d{3}\-\d{3}\-\d{4}$/;
  var toTest = $('#phone-number');
  setFieldBackground(toTest, regexpTest);
}


/**
*event handlers
*/
function registerEventHandlers() {
  $('#full-name').on('keyup', nameHandler);
  $('#birth-date').on('keyup', birthdateHandler);
  $('#phone-number').on('keyup', phoneNumberHandler);
}
$(document).ready(registerEventHandlers);
