const nit = document.getElementById("nit")
const nombre = document.getElementById("nombre")
const email = document.getElementById("email")
const pais = document.getElementById("pais")
const ciudad = document.getElementById("ciudad")
const direccion = document.getElementById("direccion")
const telefono = document.getElementById("telefono")

const boton = document.getElementById("boton")

const error_nit = document.getElementById("error_nit")
const error_nombre = document.getElementById("error_nombre")
const error_email = document.getElementById("error_email")
const error_ciudad = document.getElementById("error_ciudad")
const error_direccion = document.getElementById("error_direccion")
const error_telefono = document.getElementById("error_telefono")

boton.disabled = false
boton.style.background = "#E97451"

let validacion_nit = "si"
let validacion_nombre = "si"
let validacion_email = "si"
let validacion_pais = "si"
let validacion_ciudad = "si"
let validacion_direccion = "si"
let validacion_telefono = "si"

pais.addEventListener("input", function(){
    const valor_pais =pais.value
    console.log(valor_pais)

    if (valor_pais != ""){
        validacion_pais = "si"
        pais.style.border = "solid 1px green"
        pais.style.color = "inherit"
        activarBoton()
    }else{
        validacion_pais = "no"
        pais.style.border = "solid 1px #f00"
        
        activarBoton()
    }
})

nit.addEventListener("input", function(){
    const valor_nit = nit.value
    const verificacion_nit = /^[0-9]{10}$/

    if (valor_nit.trim() != "" && verificacion_nit.test(valor_nit)){
        nit.style.border = "solid 1px green"
        error_nit.textContent = ""
        validacion_nit = "si"
        activarBoton()
    }
    else if (valor_nit.trim() == ""){
        error_nit.textContent = "Este campo es obligatorio!";
        nit.style.border = "solid 1px red";
        error_nit.style.color = "#f00";
        validacion_nit = "no"
        activarBoton()
    }
    else if (valor_nit.length != 10){
        error_nit.textContent = "el nit debe tener 10 numeros";
        nit.style.border = "solid 1px red";
        error_nit.style.color = "#f00";
        validacion_nit = "no"
        activarBoton()
    }else{
        error_nit.textContent = "el nit solo puede tener numeros";
        nit.style.border = "solid 1px red";
        error_nit.style.color = "#f00";
        validacion_nit = "no"
        activarBoton()
    }
    
})

nombre.addEventListener("input", function(){
    const valor_nombre = nombre.value
    const verificacion_nombre = /^[a-zA-Z0-9\ ]{4,84}$/

    if (valor_nombre.trim() != "" && verificacion_nombre.test(valor_nombre)){
        nombre.style.border = "solid 1px green"
        error_nombre.textContent = ""
        validacion_nombre = "si"
        activarBoton()
    }
    else if (valor_nombre.trim() == ""){
        error_nombre.textContent = "Este campo es obligatorio!";
        nombre.style.border = "solid 1px red";
        error_nombre.style.color = "#f00";
        validacion_nombre = "no"
        activarBoton()
    }
    else if (valor_nombre.length < 4 || valor_nombre.length > 84){
        error_nombre.textContent = "el nombre debe tener entre 4 y 84 letras";
        nombre.style.border = "solid 1px red";
        error_nombre.style.color = "#f00";
        validacion_nombre = "no"
        activarBoton()
    }else{
        error_nombre.textContent = "el nombre solo puede tener letras y numeros";
        nombre.style.border = "solid 1px red";
        error_nombre.style.color = "#f00";
        validacion_nombre = "no"
        activarBoton()
    }
    
})

email.addEventListener("input", function(){
    const valor_email = email.value
    const verificacion_email = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,64}$/

    if (valor_email.trim() != "" && verificacion_email.test(valor_email)){
        email.style.border = "solid 1px green"
        error_email.textContent = ""
        validacion_email = "si"
        activarBoton()
    }
    else if (valor_email.trim() == ""){
        error_email.textContent = "Este campo es obligatorio!";
        email.style.border = "solid 1px red";
        error_email.style.color = "#f00";
        validacion_email = "no"
        activarBoton()
    }
    else if (valor_email.length < 11 || valor_email.length > 64){
        error_email.textContent = "el email debe tener entre 11 y 64 caracteres";
        email.style.border = "solid 1px red";
        error_email.style.color = "#f00";
        validacion_email = "no"
        activarBoton()
    }else{
        error_email.textContent = "esto no parece un correo electronico";
        email.style.border = "solid 1px red";
        error_email.style.color = "#f00";
        validacion_email = "no"
        activarBoton()
    }
    
}) 

ciudad.addEventListener("input", function(){
    const valor_ciudad = ciudad.value
    const verificacion_ciudad = /^[a-zA-Z\ ]{1,59}$/

    if (valor_ciudad.trim() != "" && verificacion_ciudad.test(valor_ciudad)){
        ciudad.style.border = "solid 1px green"
        error_ciudad.textContent = ""
        validacion_ciudad = "si"
        activarBoton()
    }
    else if (valor_ciudad.trim() == ""){
        error_ciudad.textContent = "Este campo es obligatorio!";
        ciudad.style.border = "solid 1px red";
        error_ciudad.style.color = "#f00";
        validacion_ciudad = "no"
        activarBoton()
    }
    else if (valor_ciudad.length < 1 || valor_ciudad.length > 59){
        error_ciudad.textContent = "la ciudad debe contener entre 1 y 59 caracteres";
        ciudad.style.border = "solid 1px red";
        error_ciudad.style.color = "#f00";
        validacion_ciudad = "no"
        activarBoton()
    }else{
        error_ciudad.textContent = "la ciudad solo debe contener letras ";
        ciudad.style.border = "solid 1px red";
        error_ciudad.style.color = "#f00";
        validacion_ciudad = "no"
        activarBoton()
    }
    
})

direccion.addEventListener("input", function(){
    const valor_direccion = direccion.value
    const verificacion_direccion = /^[a-zA-Z0-9\#\-\ ]{2,169}$/

    if (valor_direccion.trim() != "" && verificacion_direccion.test(valor_direccion)){
        direccion.style.border = "solid 1px green"
        error_direccion.textContent = ""
        validacion_direccion = "si"
        activarBoton()
    }
    else if (valor_direccion.trim() == ""){
        error_direccion.textContent = "Este campo es obligatorio!";
        direccion.style.border = "solid 1px red";
        error_direccion.style.color = "#f00";
        validacion_direccion = "no"
        activarBoton()
    }
    else if (valor_direccion.length < 2 || valor_direccion.length > 169){
        error_direccion.textContent = "la direccion debe contener entre 2 y 169 caracteres";
        direccion.style.border = "solid 1px red";
        error_direccion.style.color = "#f00";
        validacion_direccion = "no"
        activarBoton()
    }else{
        error_direccion.textContent = "esto no parece una direccion";
        direccion.style.border = "solid 1px red";
        error_direccion.style.color = "#f00";
        validacion_direccion = "no"
        activarBoton()
    }
    
})

telefono.addEventListener("input", function(){
    const valor_telefono = telefono.value
    const verificacion_telefono = /^[0-9]{10}$/

    if (valor_telefono.trim() != "" && verificacion_telefono.test(valor_telefono)){
        telefono.style.border = "solid 1px green"
        error_telefono.textContent = ""
        validacion_telefono = "si"
        activarBoton()
    }
    else if (valor_telefono.trim() == ""){
        error_telefono.textContent = "Este campo es obligatorio!";
        telefono.style.border = "solid 1px red";
        error_telefono.style.color = "#f00";
        validacion_telefono = "no"
        activarBoton()
    }
    else if (valor_telefono.length != 10){
        error_telefono.textContent = "el numero de telefono debe contener 10 numeros ";
        telefono.style.border = "solid 1px red";
        error_telefono.style.color = "#f00";
        validacion_telefono = "no"
        activarBoton()
    }else{
        error_telefono.textContent = "el numero de telefono solo debe tener numeros";
        telefono.style.border = "solid 1px red";
        error_telefono.style.color = "#f00";
        validacion_telefono = "no"
        activarBoton()
    }
    
})

function activarBoton(){

    if (validacion_nit == "si" && validacion_nombre == "si" && validacion_email == "si" && validacion_pais == "si" && validacion_ciudad == "si" && validacion_direccion == "si" && validacion_telefono == "si"){
        boton.disabled = false
        boton.style.background = "#E97451"
    }
    else{
        boton.disabled = true
        boton.style.background = "#36454F"
    }
}