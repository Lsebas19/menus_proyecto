const nombre = document.getElementById("nombre");
const campo = document.getElementById('campo_error');
const boton = document.getElementById("boton");
boton.disabled = true;

let respuesta_menus = []
nombre.addEventListener('input',function(){
    const valor = nombre.value;
    const validacion = /^[a-zA-Z/ ]{5,58}$/;

    

    if (valor.trim() !== '' && validacion.test(valor)){

        let encontrado = "no"
        for (let i = 0; i < respuesta_menus.length; i++){
            const menu = respuesta_menus[i][1];
            if(menu.trim() === valor.trim()){
                encontrado = "si"
            }
        }

        if (encontrado == "si"){
            campo.textContent = "Este menú ya existe";
            nombre.style.border = "solid 1px red";
            campo.style.color = "#f00";
            boton.style.background = "#36454F";
            boton.disabled = true;
        }else{
            campo.textContent = "";
            campo.style.color = "green";
            nombre.style.border = "solid 1px green";
            boton.style.background = "#E97451";
            boton.disabled = false;
        }

    }else if (valor.trim() == ''){
        campo.textContent = "Este campo es obligatorio!";
        nombre.style.border = "solid 1px red";
        campo.style.color = "#f00";
        boton.style.background = "#36454F";
        boton.disabled = true;
    }

    else if (valor.length < 5 || valor.length > 58){
        campo.textContent = "el dato debe tener entre 5 y 58 letras";
        nombre.style.border = "solid 1px red";
        campo.style.color = "#f00";
        boton.style.background = "#36454F";
        boton.disabled = true;
    }

    else{
        
        campo.textContent = "Este campo solo puede contener letras";
        nombre.style.border = "solid 1px red";
        campo.style.color = "#f00";
        boton.style.background = "#36454F";
        boton.disabled = true;
    };

})



async function traerMenus () {

    // Petición GET al microservicio de productos
    const response = await fetch("/traerMenus", { method: 'GET' });
    const respuesta = await response.json();
    respuesta_menus = respuesta.menus
    console.log(respuesta.menus[0])
    
}

window.onload = () => {
            traerMenus();
};
