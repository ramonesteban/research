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


$(function(){
  $.ajaxSetup({
    beforeSend: function(xhr) {
      var token = $('meta[name="csrf-token"]').attr('content');
      if (token) xhr.setRequestHeader('X-CSRF-Token', token);
    }
  });
});

$(document).ready(function() {
if (window.File && window.FileReader && window.FileList && window.Blob) {
    document.getElementById('picture').onchange = function(){
        var files = document.getElementById('picture').files;
        for(var i = 0; i < files.length; i++) {
            resizeAndUpload(files[i]);
        }
    };
} else {
    alert('The File APIs are not fully supported in this browser.');
}
});

function resizeAndUpload(file) {
var reader = new FileReader();
    reader.onloadend = function() {
 
    var tempImg = new Image();
    tempImg.src = reader.result;
    tempImg.onload = function() {
 
        var MAX_WIDTH = 800;
        var MAX_HEIGHT = 800;
        var tempW = tempImg.width;
        var tempH = tempImg.height;
        if (tempW > tempH) {
            if (tempW > MAX_WIDTH) {
               tempH *= MAX_WIDTH / tempW;
               tempW = MAX_WIDTH;
            }
        } else {
            if (tempH > MAX_HEIGHT) {
               tempW *= MAX_HEIGHT / tempH;
               tempH = MAX_HEIGHT;
            }
        }
 
        var canvas = document.createElement('canvas');
        canvas.width = tempW;
        canvas.height = tempH;
        var ctx = canvas.getContext("2d");
        ctx.drawImage(this, 0, 0, tempW, tempH);
        var dataURL = canvas.toDataURL("image/jpeg");
        console.log(dataURL);
 
        console.log('hola');
        remoteAction('/test', dataURL);
        xhr = new XMLHttpRequest();
        var token = $('meta[name="csrf-token"]').attr('content');
        xhr.onreadystatechange = function(ev){
            document.getElementById('preview-container').innerHTML = 'Done!';
        };
 
        xhr.open('POST', '/test', true);
        if (token) xhr.setRequestHeader('X-CSRF-Token', token);
        xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded");
        var data = 'image=' + dataURL;
        xhr.send(dataURL);
      }
 
   }
   reader.readAsDataURL(file);
}
