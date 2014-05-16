$(function(){
  $.ajaxSetup({
    beforeSend: function(xhr) {
      var token = $('meta[name="csrf-token"]').attr('content');
      if (token) xhr.setRequestHeader('X-CSRF-Token', token);
    }
  });
});

$(document).ajaxStart(function() {
  $('#text-container').show();
});

function remoteAction(controller, code) {
  $.ajax({
    url: controller,
    type: 'POST',
    dataType: 'json',
    data: {image: code},
    success: function(data, textStatus, xhr) {
      if (data.status == 'ok') {
        console.log(data.msg);
        console.log(data.txt);
        $('#preview-container').hide();
        $('#text-container').text(data.txt);
        if (data.res !== undefined) {
          res = 'Evaluation pass with <strong>'+data.res+'</strong>';
          $('#result-container').html(res).show();
        }
      }
      if (data.status == 'error') {
        console.log(data.msg);
      }
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
        $('#result-container').html('').hide();
        $('#text-container').text('Retrieving text...').show();
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
      var MAX_WIDTH = 1200;
      var MAX_HEIGHT = 1200;
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
