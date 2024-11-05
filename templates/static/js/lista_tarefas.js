// script.js
function mostrarDescricao(descricao) {
    document.getElementById("descricao-tarefa").innerText = descricao;
    document.getElementById("modal").style.display = "block";
}

function fecharModal() {
    document.getElementById("modal").style.display = "none";
}
