const URL = "http://10.128.66.31:3000/";

const btnAdd = document.querySelector('.btn-add');
btnCancel.addEventListener('click', function() {
  window.location.href = ('/report');
});

const btnCancel = document.querySelector('.btn-cancel');
btnCancel.addEventListener('click', function() {
  window.location.href = ('/about');
});

function changeDobotStatus(button) {
    if (button.className == "btn-off") {
    button.className = "btn-on";
    button.innerHTML = "Parar";
    fetch("http://10.128.66.238:3000/" + "on")
    .then(function (data) {
        document.getElementById("error").style.display = "none";
        button.className = "btn-off";
        button.innerHTML = "Iniciar Rotina";
    })
    .catch(function (err) {
        document.getElementById("error").innerHTML = "";
        document.getElementById("error").style.display = "block";
        document.getElementById("error").innerHTML +=" - "+ err;
        console.log("Fetch Error :-S", err);
    });
    } else {
        button.className = "btn-off";
        button.innerHTML = "Iniciar Rotina";

    fetch("http://10.128.66.238:3000/" + "stop")
    .then(function (data) {
        document.getElementById("error").style.display = "none";
    })
    .catch(function (err) {
        document.getElementById("error").innerHTML = "";
        document.getElementById("error").innerHTML +=" - "+ err;
        console.log("Fetch Error :-S", err);
    });
    }
}

// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}