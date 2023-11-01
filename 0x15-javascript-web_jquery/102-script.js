$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const langCode = $('INPUT#language_code').val();
    $.ajax({
      type: 'GET',
      url: 'https://hellosalut.stefanbohacek.dev/?cc=' + langCode,
      success: function (data) {
        $('DIV#hello').text(data.hello);
      }
    });
  });
});
