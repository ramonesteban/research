$(function(){
  $.ajaxSetup({
    beforeSend: function(xhr) {
      var token = $('meta[name="csrf-token"]').attr('content');
      if (token) xhr.setRequestHeader('X-CSRF-Token', token);
    }
  });
});

function remoteAction(controller, code) {
  $.ajax({
    url: controller,
    type: 'POST',
    dataType: 'json',
    data: {image: code},
    success: function(data, textStatus, xhr) {
      console.log(data.status);
      console.log(data.message);
    }
  });
}

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

  if (window.File && window.FileReader && window.FileList && window.Blob) {
      document.getElementById('picture').onchange = function() {
        var files = document.getElementById('picture').files;
        for(var i = 0; i < files.length; i++) {
          resizeAndUpload(files[i]);
        }
      };
  } else {
    alert('The File API are not fully supported in this browser.');
  }
});

function resizeAndUpload(file) {
  var reader = new FileReader();

  reader.onloadend = function() { 
    var tmp_image = new Image();
    tmp_image.src = reader.result;
    tmp_image.onload = function() {
      var MAX_WIDTH = 800;
      var MAX_HEIGHT = 800;
      var tmpW = tmp_image.width;
      var tmpH = tmp_image.height;

      if (tmpW > tmpH) {
        if (tmpW > MAX_WIDTH) {
           tmpH *= MAX_WIDTH / tmpW;
           tmpW = MAX_WIDTH;
        }
      } else {
        if (tmpH > MAX_HEIGHT) {
           tmpW *= MAX_HEIGHT / tmpH;
           tmpH = MAX_HEIGHT;
        }
      }

      var canvas = document.createElement('canvas');
      canvas.width = tmpW;
      canvas.height = tmpH;
      var ctx = canvas.getContext("2d");
      ctx.drawImage(this, 0, 0, tmpW, tmpH);
      var dataURL = canvas.toDataURL("image/jpeg");

      remoteAction('/upload_image', dataURL);
    }
  }
  reader.readAsDataURL(file);
}
