if (!localStorage.getItem('refresh')) {
    localStorage.setItem('refresh', "0");
}
const path = window.location.pathname;
const page = path.split("/").pop();

document.addEventListener('DOMContentLoaded', function () {

    //mostra os só os resultados depois de refresh a pagina
    if (page === "comentarios") {
        if(localStorage.getItem('refresh') === "0") {
            document.querySelector('form').style.display = "block";
        } else {
            document.querySelector('form').style.display = "none";
            localStorage.setItem('refresh', "0");
        }
    } else {
        //para o caso de ele ir embora da página
        localStorage.setItem('refresh', "0");
    }

    // Alerta com mensagem diferente para cada um dos formulários
    document.querySelector('form').onsubmit = function () {
        if (page === "comentarios") {
            alert("Comentario submetido. Veja os resultados gerais.");
            localStorage.setItem('refresh',"1");
        }

        if (page === "quizz") {
            alert("Quizz submetido. Clique no OK para ver os seus resultados.");
        }

        if (page === "contacto") {
            alert("Contacto submetido. Iremos contactá-lo em breve.");
        }
    }
})