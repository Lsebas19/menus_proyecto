const identidad = document.getElementById("identidad")
const nombre = document.getElementById("nombre")
const email = document.getElementById("email")
const contrasena = document.getElementById("contrasena")
const confirmar_contrasena = document.getElementById("confirmar_contrasena")
const boton = document.getElementById("boton")

let validacion_identidad = "no"
let validacion_nombre = "no"
let validacion_email = "no"
let validacion_contrasena = "no"
let validacion_confirmar_contrasena = "no"

boton.disabled = true
boton.style.background = "grey"

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
contrasena.addEventListener("input", function(){
    const valor_contrasena = contrasena.value
    const valor_confirmar_contrasena = confirmar_contrasena.value
    const verificacion_contrasena = /^[a-zA-Z0-9/]{6,12}$/
    const campo_error_contrasena=document.getElementById("campo_error_contrasena")
    const campo_error_confirmar_contrasena=document.getElementById("campo_error_confirmar_contrasena")

    if (valor_contrasena.trim() !== '' && verificacion_contrasena.test(valor_contrasena)){

        if (valor_contrasena != valor_confirmar_contrasena){
            campo_error_confirmar_contrasena.textContent = "las contraseñas no coinciden ";
            campo_error_contrasena.textContent = "";
            contrasena.style.border = "solid 1px red";
            campo_error_contrasena.style.color = "#f00";
            validacion_contrasena = "no"
            
            confirmar_contrasena.style.border = "solid 1px red";
            campo_error_confirmar_contrasena.style.color = "#f00";
            validacion_confirmar_contrasena = "no"
            activarBoton()
        }
        else{
            campo_error_contrasena.textContent = "";
            campo_error_contrasena.style.color = "green";
            contrasena.style.border = "solid 1px green";
            confirmar_contrasena.style.border = "solid 1px green";
            campo_error_confirmar_contrasena.textContent = ""
            validacion_contrasena = "si"
            validacion_confirmar_contrasena = "si"
            activarBoton()
        }
        
        
    
    }else if (valor_contrasena.trim() == ''){
        campo_error_contrasena.textContent = "Este campo es obligatorio!";
        contrasena.style.border = "solid 1px red";
        campo_error_contrasena.style.color = "#f00";
        validacion_contrasena = "no"
        activarBoton()
    }

    else if (valor_contrasena.length < 6 || valor_contrasena.length > 12){
        campo_error_contrasena.textContent = "el dato debe tener entre 6 y 12 caracteres";
        contrasena.style.border = "solid 1px red";
        campo_error_contrasena.style.color = "#f00";
        validacion_contrasena = "no"
        activarBoton()
    }
    

    else{
        
        campo_error_contrasena.textContent = "Este campo solo puede contener letras y numeros";
        contrasena.style.border = "solid 1px red";
        campo_error_contrasena.style.color = "#f00";
        validacion_contrasena = "no"
        activarBoton()
    };

})

confirmar_contrasena.addEventListener("input", function(){
    const valor_confirmar_contrasena = confirmar_contrasena.value
    const verificacion_contrasena = /^[a-zA-Z0-9/]{6,12}$/
    
    const campo_error_confirmar_contrasena=document.getElementById("campo_error_confirmar_contrasena")

    const campo_error_contrasena=document.getElementById("campo_error_contrasena")
    const valor_contrasena = contrasena.value

    if (valor_contrasena.trim() !== '' && verificacion_contrasena.test(valor_contrasena)){

        if (valor_contrasena != valor_confirmar_contrasena ){
            campo_error_confirmar_contrasena.textContent = "las contraseñas no coinciden ";
            campo_error_contrasena.textContent = "";
            contrasena.style.border = "solid 1px red";
            campo_error_contrasena.style.color = "#f00";
            validacion_contrasena = "no"
            
            confirmar_contrasena.style.border = "solid 1px red";
            campo_error_confirmar_contrasena.style.color = "#f00";
            validacion_confirmar_contrasena = "no"
            activarBoton()
        }
        else{
            campo_error_confirmar_contrasena.textContent = "";
            campo_error_confirmar_contrasena.style.color = "green";
            confirmar_contrasena.style.border = "solid 1px green";
            contrasena.style.border = "solid 1px green";
            validacion_confirmar_contrasena = "si"
            validacion_contrasena = "si"
            activarBoton()
        }
    }
    else if (valor_contrasena.trim() == ''){
        campo_error_contrasena.textContent = "Este campo es obligatorio!";
        contrasena.style.border = "solid 1px red";
        campo_error_contrasena.style.color = "#f00";
        validacion_contrasena = "no"
        activarBoton()
    }

    else if (valor_contrasena.length < 6 || valor_contrasena.length > 12){
        campo_error_contrasena.textContent = "el dato debe tener entre 6 y 12 caracteres";
        contrasena.style.border = "solid 1px red";
        campo_error_contrasena.style.color = "#f00";
        validacion_contrasena = "no"
        activarBoton()
    }
    

    else{
        
        campo_error_contrasena.textContent = "Este campo solo puede contener letras y numeros";
        contrasena.style.border = "solid 1px red";
        campo_error_contrasena.style.color = "#f00";
        validacion_contrasena = "no"
        activarBoton()
    };
        

})

function activarBoton(){
    console.log(validacion_identidad)
    console.log(validacion_nombre)
    console.log(validacion_email)
    console.log(validacion_contrasena)
    console.log(validacion_confirmar_contrasena)
    
    if (validacion_identidad == "si" && validacion_nombre == "si" && validacion_email == "si" && validacion_contrasena == "si" && validacion_confirmar_contrasena == "si"){
        boton.disabled = false
        boton.style.background = "#E97451"
    }
    else{
        boton.disabled = true
        boton.style.background = "#36454F"
    }
}

const formulario = document.getElementById("formularioUsuario")

formulario.addEventListener('submit', async function (event) {
    
    event.preventDefault();
    const id = document.getElementById("identidad").value
    // Petición GET al microservicio de productos
    const response = await fetch("/verificarNumeroIdentidad/"+id, { method: 'GET' });
    const respuesta = await response.json();
    
    if (respuesta.mensaje == "si"){
        event.target.submit()
    }else{
        const campo_error_identidad = document.getElementById("campo_error_identidad")

        campo_error_identidad.textContent = "el usuario ya existe"
        campo_error_identidad.style.color = "red"
        document.getElementById("identidad").style.border = "solid 1px red"
    }
    

})