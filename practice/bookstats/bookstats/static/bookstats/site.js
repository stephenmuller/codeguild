'use strict';

var wordSource = $('#word-source');


function updateIndex(statsObj) {
    var statsContainer = $('#display_stats');
    var statsDisplay = $('<p>' statsObj.word + ' occurs ' + statsObj.word_count + ' times and is '
    + statsObj.word_frequency ' ratio of all words in book. <p>')
    statsContainer.append(statsDisplay)
}

/**
 * Submit the code form and return a promise with the JSON colored source object.
 */
function submitForm() {
  var actionURL = wordSource.attr('action');
  var submitMethod = wordSource.attr('method');
  var formData = wordSource.serialize();
  return Promise.resolve($.ajax({
    dataType: 'json',
    url: actionURL,
    method: submitMethod,
    data: formData
  }));
}

/**
 * Main function that gets data from the source form, POSTs it in the
 * background and updates the page on return.
 */
function runSubmitSourceAndUpdate() {
  // Empty the UI right away so that new data can be loaded.
  emptyResponseElements();
  submitForm().
    then(updateIndex(statsObj))
    // Decode the JSON and call the following function with the resulting JS object.
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