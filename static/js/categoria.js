const nombre = document.getElementById("nombreCategoria");
const campo = document.getElementById('campo_error');
const boton = document.getElementById("boton");
let respuesta_categorias = []
boton.disabled = true;
nombre.addEventListener('input',function(){
    const valor = nombre.value;
    const validacion = /^[a-zA-Z/ ]{5,58}$/;

    

    if (valor.trim() !== '' && validacion.test(valor)){
        
        let encontrado = "no"
        for (let i = 0; i < respuesta_categorias.length; i++){
            const categoria = respuesta_categorias[i][2];
            if(categoria.trim() === valor.trim()){
                encontrado = "si"
            }
        }

        if (encontrado == "si"){
            campo.textContent = "Esta categoria ya existe";
            nombre.style.border = "solid 1px red";
            campo.style.color = "#f00";
            boton.style.background = "#36454F";
            boton.disabled = true;
        }
        else{
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


async function traerCategorias () {

    // Petición GET al microservicio de productos
    const response = await fetch("/traerCategorias", { method: 'GET' });
    const respuesta = await response.json();
    respuesta_categorias = respuesta.categorias
    console.log(respuesta.categorias[0])
    
}

window.onload = () => {
            traerCategorias();
};