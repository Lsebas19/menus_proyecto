
const contrasena = document.getElementById("contrasena")
const confirmar_contrasena = document.getElementById("confirmar_contrasena")
const boton = document.getElementById("boton")

let validacion_contrasena_vieja = "no"
let validacion_contrasena = "no"
let validacion_confirmar_contrasena = "no"

boton.disabled = true
boton.style.background = "grey"

contrasena_vieja.addEventListener("input", function(){
    const valor_contrasena_vieja = contrasena_vieja.value
    
    const verificacion_contrasena_vieja = /^[a-zA-Z0-9/]{6,12}$/
    const campo_error_contrasena_vieja=document.getElementById("campo_error_contrasena_vieja")

    if (valor_contrasena_vieja.trim() !== '' && verificacion_contrasena_vieja.test(valor_contrasena_vieja)){

        campo_error_contrasena_vieja.textContent = "";
        campo_error_contrasena_vieja.style.color = "green";
        contrasena_vieja.style.border = "solid 1px green";
        
        validacion_contrasena_vieja = "si"
        
        activarBoton()
        
    }else if (valor_contrasena_vieja.trim() == ''){
        campo_error_contrasena_vieja.textContent = "Este campo es obligatorio!";
        contrasena_vieja.style.border = "solid 1px red";
        campo_error_contrasena_vieja.style.color = "#f00";
        validacion_contrasena_vieja = "no"
        activarBoton()
    }

    else if (valor_contrasena_vieja.length < 6 || valor_contrasena_vieja.length > 12){
        campo_error_contrasena_vieja.textContent = "el dato debe tener entre 6 y 12 caracteres";
        contrasena_vieja.style.border = "solid 1px red";
        campo_error_contrasena_vieja.style.color = "#f00";
        validacion_contrasena_vieja = "no"
        activarBoton()
    }
    

    else{
        
        campo_error_contrasena_vieja.textContent = "Este campo solo puede contener letras y numeros";
        contrasena_vieja.style.border = "solid 1px red";
        campo_error_contrasena_vieja.style.color = "#f00";
        validacion_contrasena_vieja = "no"
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
    
    
    if (validacion_contrasena == "si" && validacion_confirmar_contrasena == "si"){
        boton.disabled = false
        boton.style.background = "#E97451"
    }
    else{
        boton.disabled = true
        boton.style.background = "#36454F"
    }
}