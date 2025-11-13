const categoria = document.getElementById("categoria")
const nombre = document.getElementById("nombreProducto")
const boton = document.getElementById("boton")
const presentacion = document.getElementById("presentacion")
const descripcion = document.getElementById("descripcion")
const precio = document.getElementById("precio")

let validacion_categoria = "no"
let validacion_nombre = "no"
let validacion_descripcion = "no"
let validacion_presentacion = "no"
let validacion_precio = "no"

boton.disabled = true
let respuesta_productos = []

categoria.addEventListener("input", function(){
    const valor_categoria = categoria.value
    console.log(valor_categoria)

    if (valor_categoria != "ninguna"){
        validacion_categoria = "si"
        activarBoton()
    }else{
        validacion_categoria = "no"
        activarBoton()
    }
})

nombre.addEventListener("input", function(){
    const valor_nombre = nombre.value
    const verificacion_nombre = /^[a-zA-Z0-9/ ]{3,183}$/
    const campo_error_nombre=document.getElementById("campo_error_nombre")

    if (valor_nombre.trim() !== '' && verificacion_nombre.test(valor_nombre)){

        let encontrado = "no"
        for (let i = 0; i < respuesta_productos.length; i++){
            const producto = respuesta_productos[i][1];
            if(producto.trim() === valor_nombre.trim()){
                encontrado = "si"
            }
        }

        if (encontrado == "si"){
            campo_error_nombre.textContent = "Este producto ya existe";
            nombre.style.border = "solid 1px red";
            campo_error_nombre.style.color = "#f00";
            validacion_nombre = "no"
            activarBoton()
        }else{
            campo_error_nombre.textContent = "";
            campo_error_nombre.style.color = "green";
            nombre.style.border = "solid 1px green";
            
            validacion_nombre = "si"
            activarBoton()
        }

        
    
    }else if (valor_nombre.trim() == ''){
        campo_error_nombre.textContent = "Este campo es obligatorio!";
        nombre.style.border = "solid 1px red";
        campo_error_nombre.style.color = "#f00";
        validacion_nombre = "no"
        activarBoton()
    }

    else if (valor_nombre.length < 5 || valor_nombre.length > 15){
        campo_error_nombre.textContent = "el dato debe tener entre 3 y 183 letras";
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

descripcion.addEventListener("input", function(){
    const valor_descripcion = descripcion.value
    const verificacion_descripcion = /^[a-zA-Z0-9/,/ ]{6,150}$/
    const campo_error_descripcion=document.getElementById("campo_error_descripcion")

    if (valor_descripcion.trim() !== '' && verificacion_descripcion.test(valor_descripcion)){
        campo_error_descripcion.textContent = "";
        campo_error_descripcion.style.color = "green";
        descripcion.style.border = "solid 1px green";
        validacion_descripcion="si"
        activarBoton()
    
    }else if (valor_descripcion.trim() == ''){
        campo_error_descripcion.textContent = "Este campo es obligatorio!";
        descripcion.style.border = "solid 1px red";
        campo_error_descripcion.style.color = "#f00";
        validacion_descripcion="no"
        activarBoton()
       
    }

    else if (valor_descripcion.length < 5 || valor_descripcion.length > 15){
        campo_error_descripcion.textContent = "el dato debe tener entre 6 y 150 letras";
        descripcion.style.border = "solid 1px red";
        campo_error_descripcion.style.color = "#f00";
        validacion_descripcion="no"
        activarBoton()
    }

    else{
        campo_error_descripcion.textContent = "Este campo solo puede contener letras y numeros";
        descripcion.style.border = "solid 1px red";
        campo_error_descripcion.style.color = "#f00";
        validacion_descripcion="no"
        activarBoton()
    };

})


presentacion.addEventListener("input", function(){
    const valor_presentacion = presentacion.value
    const verificacion_presentacion = /^[a-zA-Z0-9/ ]{6,150}$/
    const campo_error_presentacion=document.getElementById("campo_error_presentacion")

    if (valor_presentacion.trim() !== '' && verificacion_presentacion.test(valor_presentacion)){
        campo_error_presentacion.textContent = "";
        campo_error_presentacion.style.color = "green";
        presentacion.style.border = "solid 1px green";
        validacion_presentacion = "si"
        activarBoton()
    
    }else if (valor_presentacion.trim() == ''){
        campo_error_presentacion.textContent = "Este campo es obligatorio!";
        presentacion.style.border = "solid 1px red";
        campo_error_presentacion.style.color = "#f00";
        validacion_presentacion = "no"
        activarBoton()
    }

    else if (valor_presentacion.length < 5 || valor_presentacion.length > 15){
        campo_error_presentacion.textContent = "el dato debe tener entre 6 y 150 letras";
        presentacion.style.border = "solid 1px red";
        campo_error_presentacion.style.color = "#f00";
        validacion_presentacion = "no"
        activarBoton()
    }

    else{
        
        campo_error_presentacion.textContent = "Este campo solo puede contener letras y numeros";
        presentacion.style.border = "solid 1px red";
        campo_error_presentacion.style.color = "#f00";
        validacion_presentacion = "no"
        activarBoton()
    };

})


precio.addEventListener("input", function(){
    const valor_precio = precio.value
    const verificacion_precio = /^[0-9]{4,6}$/
    const campo_error_precio=document.getElementById("campo_error_precio")

    if (valor_precio.trim() !== '' && verificacion_precio.test(valor_precio)){
        campo_error_precio.textContent = "";
        campo_error_precio.style.color = "green";
        precio.style.border = "solid 1px green";
        validacion_precio = "si"
        activarBoton()
    
    }else if (valor_precio.trim() == ''){
        campo_error_precio.textContent = "Este campo es obligatorio!";
        precio.style.border = "solid 1px red";
        campo_error_precio.style.color = "#f00";
        validacion_precio = "no"
        activarBoton()
    }

    else if (valor_precio.length < 5 || valor_precio.length > 15){
        campo_error_precio.textContent = "el precio debe estar entre 1.000 y 999.999";
        precio.style.border = "solid 1px red";
        campo_error_precio.style.color = "#f00";
        validacion_precio = "no"
        activarBoton()
    }

    else{
        
        campo_error_precio.textContent = "Este campo solo puede contener numeros";
        precio.style.border = "solid 1px red";
        campo_error_precio.style.color = "#f00";
        validacion_precio = "no"
        activarBoton()
    };

})

function activarBoton(){
    
    if (validacion_categoria == "si" && validacion_nombre == "si" && validacion_descripcion == "si" && validacion_presentacion == "si" && validacion_precio == "si"){
        boton.disabled = false
        boton.style.background = "#E97451"
    }
    else{
        boton.disabled = true
        boton.style.background = "#36454F"
    }
}



async function traerProductos () {

    // Petición GET al microservicio de productos
    const response = await fetch("/traerProductos", { method: 'GET' });
    const respuesta = await response.json();
    respuesta_productos = respuesta.productos
    console.log(respuesta.productos[0])
    
}

window.onload = () => {
            traerProductos();
};



// Jaramillo zone — limpieza y encapsulación
(function() {
    // DRAG & DROP - Imagen Upload (encapsulado para evitar variables globales)
    const inputImagen = document.getElementById('inputImagen');
    const infoArchivo = document.getElementById('infoArchivo');
    const vistaPrevia = document.getElementById('vistaPreviaImagen');
    const seccionImagen = document.getElementById('seccionImagen');

    // Mostrar preview cuando se selecciona archivo
    function mostrarPreview(file) {
        if (!file || !file.type || !file.type.startsWith('image/')) {
            if (infoArchivo) infoArchivo.textContent = 'Seleccione una imagen válida';
            if (vistaPrevia) {
                vistaPrevia.style.display = 'none';
                vistaPrevia.src = '';
            }
            return;
        }

        const reader = new FileReader();
        reader.onload = function(e) {
            if (vistaPrevia) {
                vistaPrevia.src = e.target.result;
                vistaPrevia.style.display = 'block';
            }
        };
        reader.readAsDataURL(file);
        if (infoArchivo) infoArchivo.textContent = file.name;
    }

    // Listener para cambios en el input file
    if (inputImagen) {
        inputImagen.addEventListener('change', function(e) {
            const file = e.target.files?.[0] ?? null;
            mostrarPreview(file);
        });
    }

    // Drag & Drop handlers (con manejadores reutilizables)
    if (seccionImagen) {
        const addDragOver = (e) => { e.preventDefault(); e.stopPropagation(); seccionImagen.classList.add('drag-over'); };
        const removeDragOver = (e) => { e.preventDefault(); e.stopPropagation(); seccionImagen.classList.remove('drag-over'); };

        seccionImagen.addEventListener('dragover', addDragOver);
        seccionImagen.addEventListener('dragenter', addDragOver);
        seccionImagen.addEventListener('dragleave', removeDragOver);

        seccionImagen.addEventListener('drop', (e) => {
            e.preventDefault();
            e.stopPropagation();
            seccionImagen.classList.remove('drag-over');

            const files = e.dataTransfer?.files;
            if (files && files.length > 0 && inputImagen) {
                // Algunos navegadores no permiten asignar files directamente; intentamos y si falla usamos DataTransfer
                try {
                    inputImagen.files = files;
                } catch (err) {
                    const dt = new DataTransfer();
                    for (let i = 0; i < files.length; i++) dt.items.add(files[i]);
                    inputImagen.files = dt.files;
                }
                // Disparar evento change manualmente
                const event = new Event('change', { bubbles: true });
                inputImagen.dispatchEvent(event);
            }
        });
    }
})(); 


    