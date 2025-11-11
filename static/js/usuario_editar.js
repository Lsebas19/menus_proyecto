const identidad = document.getElementById("identidad")
const nombre = document.getElementById("nombre")
const email = document.getElementById("email")

const boton = document.getElementById("boton")

let validacion_identidad = "si"
let validacion_nombre = "si"
let validacion_email = "si"


boton.disabled = false
boton.style.background = "#E97451"

identidad.addEventListener("input", function(){
    const valor_identidad = identidad.value
    const verificacion_identidad = /^[a-zA-Z0-9/]{6,15}$/
    const campo_error_identidad=document.getElementById("campo_error_identidad")

    if (valor_identidad.trim() !== '' && verificacion_identidad.test(valor_identidad)){
        
        campo_error_identidad.textContent = "";
        campo_error_identidad.style.color = "green";
        identidad.style.border = "solid 1px green";
        
        validacion_identidad = "si"
        activarBoton()
        
    
    }else if (valor_identidad.trim() == ''){
        campo_error_identidad.textContent = "Este campo es obligatorio!";
        identidad.style.border = "solid 1px red";
        campo_error_identidad.style.color = "#f00";
        validacion_identidad = "no"
        activarBoton()
    }

    else if (valor_identidad.length < 6 || valor_identidad.length > 15){
        campo_error_identidad.textContent = "el dato debe tener entre 6 y 15 numeros y letras";
        identidad.style.border = "solid 1px red";
        campo_error_identidad.style.color = "#f00";
        validacion_identidad = "no"
        activarBoton()
    }

    else{
        
        campo_error_identidad.textContent = "Este campo solo puede contener numeros y letras";
        identidad.style.border = "solid 1px red";
        campo_error_identidad.style.color = "#f00";
        validacion_identidad = "no"
        activarBoton()
    };

})

nombre.addEventListener("input", function(){
    const valor_nombre = nombre.value
    const verificacion_nombre = /^[a-zA-Z0-9/ ]{1,85}$/
    const campo_error_nombre=document.getElementById("campo_error_nombre")

    if (valor_nombre.trim() !== '' && verificacion_nombre.test(valor_nombre)){
        campo_error_nombre.textContent = "";
        campo_error_nombre.style.color = "green";
        nombre.style.border = "solid 1px green";
        
        validacion_nombre = "si"
        activarBoton()
        
    
    }else if (valor_nombre.trim() == ''){
        campo_error_nombre.textContent = "Este campo es obligatorio!";
        nombre.style.border = "solid 1px red";
        campo_error_nombre.style.color = "#f00";
        validacion_nombre = "no"
        activarBoton()
    }

    else if (valor_nombre.length < 1 || valor_nombre.length > 85){
        campo_error_nombre.textContent = "el dato debe tener entre 1 y 85 letras";
        nombre.style.border = "solid 1px red";
        campo_error_nombre.style.color = "#f00";
        validacion_nombre = "no"
        activarBoton()
    }

    else{
        
        campo_error_nombre.textContent = "Este campo solo puede contener letras y numeros";
        nombre.style.border = "solid 1px red";
        campo_error_nombre.style.color = "#f00";
        validacion_nombre = "no"
        activarBoton()
    };

})


email.addEventListener("input", function(){
    const valor_email = email.value
    const verificacion_email = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,64}$/
    const campo_error_email=document.getElementById("campo_error_email")

    if (valor_email.trim() !== '' && verificacion_email.test(valor_email)){
        campo_error_email.textContent = "";
        campo_error_email.style.color = "green";
        email.style.border = "solid 1px green";
        
        validacion_email = "si"
        activarBoton()
        
    
    }else if (valor_email.trim() == ''){
        campo_error_email.textContent = "Este campo es obligatorio!";
        email.style.border = "solid 1px red";
        campo_error_email.style.color = "#f00";
        validacion_email = "no"
        activarBoton()
    }

    else if (valor_email.length < 11 || valor_email.length > 64){
        campo_error_email.textContent = "el dato debe tener entre 11 y 64 caracteres";
        email.style.border = "solid 1px red";
        campo_error_email.style.color = "#f00";
        validacion_email = "no"
        activarBoton()
    }

    else{
        
        campo_error_email.textContent = "Esto no parece un correo electronico";
        email.style.border = "solid 1px red";
        campo_error_email.style.color = "#f00";
        validacion_email = "no"
        activarBoton()
    };

})

function activarBoton(){
    
    if (validacion_identidad == "si" && validacion_nombre == "si" && validacion_email == "si" ){
        boton.disabled = false
        boton.style.background = "#E97451"
    }
    else{
        boton.disabled = true
        boton.style.background = "#36454F"
    }
}