$('document').ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?', function (data) {
    $('DIV#hello').text(data.hello);
  });
});
