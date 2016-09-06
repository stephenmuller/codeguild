'use strict';

var wordSource = $('#word-source');

/**
 * Submit the code form and return a promise with the JSON colored source object.
 */
function submitForm() {
  var actionURL = sourceForm.attr('action');
  var submitMethod = sourceForm.attr('method');
  var formData = sourceForm.serialize();
  return Promise.resolve($.ajax({
    dataType: 'json',
    url: actionURL,
    method: submitMethod,
    data: formData
  }));
}


/**
 * Register form submit event handler.
 */
function registerGlobalEventHandlers() {
  sourceForm.on('submit', function(event) {
    event.preventDefault();
    runSubmitSourceAndUpdate();
  });
}

// Register handlers for permanent elements on the page.
$(document).ready(registerGlobalEventHandlers);