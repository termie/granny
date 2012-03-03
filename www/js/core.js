function displayPeople (data, textStatus, jqXHR) {
  $('#people').empty()
  $(data).each(function (index, person) {
    $('#people').append(
        '<div class="row"><div class="span6">' + person.name + '</div></div>')

  })
}

$(function () {
  $.getJSON('wordy.json', displayPeople)
})
