function deleteEntry(url) {
    var token = $('input').val();

    $.ajax({
        url: url,
        type: 'DELETE',
        beforeSend: function(xhr) {
            xhr.setRequestHeader("X-CSRFToken", token);
        }
    });
}

function registerEventHandlers() {
  $('li a').on('click', function(e) {
    e.preventDefault();
    console.dir(e.currentTarget.href);
    deleteEntry(e.currentTarget.href);
    window.location = window.location;
  });
};

$(document).ready(registerEventHandlers);
