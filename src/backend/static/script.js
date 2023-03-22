const URL = "http://127.0.0.1:3000/";

function changeDobotStatus(button) {

    if (button.className == "btn-off") {
    fetch(URL + "on")
    .then(function (data) {
        document.getElementById("error").style.display = "none";
        
        button.className = "btn-on";
        button.innerHTML = "Parar";
    })
    .catch(function (err) {
        document.getElementById("error").innerHTML = "";
        document.getElementById("error").style.display = "block";
        document.getElementById("error").innerHTML +=" - "+ err;
        console.log("Fetch Error :-S", err);
    });
    } else {
    fetch(URL + "stop")
    .then(function (data) {
        document.getElementById("error").style.display = "none";

        button.className = "btn-off";
        button.innerHTML = "Iniciar Rotina";
    })
    .catch(function (err) {
        document.getElementById("error").innerHTML +=" - "+ err;

        console.log("Fetch Error :-S", err);
    });
    }
}