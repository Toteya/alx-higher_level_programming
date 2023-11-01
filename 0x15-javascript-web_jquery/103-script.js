$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    makeRequest();
  });
  $('INPUT#language_code').on('keypress', function (e) {
    if (e.which === 13) {
      $('INPUT#btn_translate').trigger('click');
    }
  });
});

function makeRequest () {
  const langCode = $('INPUT#language_code').val();
  $.ajax({
    type: 'GET',
    url: 'https://hellosalut.stefanbohacek.dev/?cc=' + langCode,
    success: function (data) {
      $('DIV#hello').text(data.hello);
    }
  });
}
