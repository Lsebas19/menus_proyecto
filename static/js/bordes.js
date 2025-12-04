// ====== MENÚ HAMBURGUESA ======
function hamburguesa(){
    const btnHamburguesa = document.getElementById("menu_ham");
    const barraLateral = document.querySelector("aside");
    const vidrio = document.getElementById("vidrio");
    let abiertaPorClick = false;

    // Inicializar barra lateral cerrada
    barraLateral.classList.add("contraida");

    btnHamburguesa.addEventListener("click", (e) => {
        e.preventDefault();
        abiertaPorClick = !abiertaPorClick;
        btnHamburguesa.classList.toggle("activo");
        
        if (abiertaPorClick) {
            barraLateral.classList.remove("contraida");
            barraLateral.classList.add("abierta");
            vidrio.classList.add("activo");
        } else {
            barraLateral.classList.remove("abierta");
            barraLateral.classList.add("contraida");
            vidrio.classList.remove("activo");
        }
    });

    // Cerrar sidebar al hacer click en el vidrio
    vidrio.addEventListener("click", () => {
        if (abiertaPorClick && btnHamburguesa) {
            abiertaPorClick = false;
            btnHamburguesa.classList.remove("activo");
            barraLateral.classList.remove("abierta");
            barraLateral.classList.add("contraida");
            vidrio.classList.remove("activo");
        }
    });

    // Cerrar sidebar al hacer click en un link
    const enlaces = document.querySelectorAll("aside a");
    enlaces.forEach(enlace => {
        enlace.addEventListener("click", () => {
            if (abiertaPorClick && btnHamburguesa) {
                abiertaPorClick = false;
                btnHamburguesa.classList.remove("activo");
                barraLateral.classList.remove("abierta");
                barraLateral.classList.add("contraida");
                vidrio.classList.remove("activo");
            }
        });
    });
}

document.addEventListener("DOMContentLoaded", ()=>{

    hamburguesa();

});