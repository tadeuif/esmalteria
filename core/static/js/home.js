console.log('Hello!')

function toggleSidebar(){
    document.getElementById("sidebar").classList.toggle('active');
}

function mudaText(){
    var texto = document.getElementById("teste")
    texto.textContent = "TESTE"
}