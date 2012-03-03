function displayPeople (data, textStatus, jqXHR) {
  $('#people').empty()
  $(data).each(function (index, person) {
    $('#people').append(
        '<div class="row person"><div class="span4 offset1 person-name">' + person.name + '</div><div class="span4 person-score">' + person.score + '</div></div>')

  })
}

$(function () {
  $.getJSON('wordy.json', displayPeople)
})
