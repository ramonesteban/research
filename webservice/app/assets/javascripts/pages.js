function readURL(input) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();

    reader.onload = function(e) {
      $('#preview-image').attr('src', e.target.result);
      $('#preview-container').show();
    }

    reader.readAsDataURL(input.files[0]);
  }
}

$(document).ready(function() {
  $('#picture').change(function() {
    readURL(this);
  });
});
