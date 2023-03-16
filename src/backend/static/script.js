const URL = "http://127.0.0.1:3000/";

const informations = `
    <p class="title">Relatório</p>
    <p class="sub-title">Preencha as informações relacionadas a amostra em análise</p>
    <div class="input-group">
        <label for="projeto">Projeto</label>
        <input type="text" name="projeto" id="projeto">
    </div>
    <div class="input-group">
        <label for="amostra">Amostra</label>
        <input type="text" name="amostra" id="amostra">
    </div>
    <div class="input-group">
        <label for="data">Data</label>
        <input style="width: 30%;" type="date" name="data" id="data">
    </div>
    <div style="display: flex;">
        <div class="input-group" style="margin-right: 10%;">
            <label for="material">Material</label>
            <input style="width: 100%;" type="text" name="data" id="data">
        </div>
        <div class="input-group">
            <label for="massa">Massa (gramas)</label>
            <input style="width: 100%;" type="text" name="data" id="data">
        </div>
    </div>
    <div class="button-group">
        <a href="" class="btn-cancel">Cancelar</a>
        <a class="btn-add" onclick="toggleContent()">Adicionar</a>
    </div>
`

const routine = `
    <div class="info-label">
        <p>Projeto: <span class="info-span-label">IPT Inteli Colab</span></p>
        <p>Amostra: <span class="info-span-label">Ferro-Cromo</span></p>
        <p>Data: <span class="info-span-label">16/03/2023</span> </p>
    </div>
    <div class="container-btn">
        <button onclick="changeDobotStatus(this)" class="btn-off">
        Iniciar rotina
        </button>
    </div>
    <p id="error">Error</p>
    <div class="dobot">
        <div class="seletion-group">
            <div class="">
            <p class="title">Dobot Magician Lite</p>
            <p class="sub-title">Flask app v1.4</p>
                <div class="slider">
                    <label for="fader">Ímã</label>
                    <input type="range" min="0" max="3" value="0" id="fader"oninput="rangeValue.innerText = this.value">
                    <p id="rangeValue">0</p>
                </div>
            </div>
        </div>
    </div>
    <div class="report">
        <a class="report-btn" onclick="toggleContent()">
            <div class="report-text">
                Gerar relatório
            </div>
            <div class="report-img">
                <img class="next" src="../static/images/right-arrow.png">
            </div>
        </a>
    </div>
`
window.addEventListener('load', function (){
    const form = document.getElementById("form");
    form.innerHTML = informations;
})

function toggleContent(){
    const form = document.getElementById("form")
    if(form.innerHTML === informations){
        form.innerHTML = routine
    } else {
        form.innerHTML = informations
    }
}

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