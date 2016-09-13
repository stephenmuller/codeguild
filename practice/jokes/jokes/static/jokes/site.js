'use strict';


function initializeEventHandlers() {
  $('.rootelement').on('click', function(event){
    $(this).children('.punchline').show();
  })
}


$(document).on('ready', initializeEventHandlers);
