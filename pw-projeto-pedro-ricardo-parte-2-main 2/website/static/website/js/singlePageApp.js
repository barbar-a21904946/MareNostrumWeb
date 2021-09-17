const path = window.location.pathname;
const page = path.split("/").pop();

// primeira seccao
let counter = 0;

// carregar 3 secções ao inicio
let quantity = 3;
if(page === "about") {
    quantity = 5;
}

// Quando o DOM carrega carregar as 3 primeiras secções
document.addEventListener('DOMContentLoaded', load);

// Se der scroll até ao fim carregar mais 1
window.onscroll = () => {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
        quantity = 1;
        load();
    }
};

function load() {

    const start = counter
    const end = start + quantity - 1;
    counter = end + 1;

    fetch(`/seccoes?start=${start}&end=${end}`)
    .then(response => response.json())
    .then(data => {
        data.seccoes.forEach(add_post);
    });
};

function add_post(contents) {
   document.getElementById(contents).style.display = "block";
};