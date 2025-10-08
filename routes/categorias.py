from conexion import *
from models.categorias import *
from models.productos import *

#ruta donde se visualizan todas las categorias de cada empresa
@web_app.route("/categorias")
def categorias():
    #verifica si la sesion está iniciada
    if session.get("login") == True:
        #busca los productos con sus respectivas categorias
        productos_resultado=mi_producto.buscarProductosConCategoria()

        #redirigir a crear empresa si el usuario no tiene
        if productos_resultado == "no tiene empresa":
            return redirect("/crearEmpresa")

        #busca todas las categorias que le correspondan a la empresa del usuario logueado
        resultado = mi_categoria.buscarCategorias()

        
        #renderiza el html de categorias con los datos recolectados
        return render_template("categorias.html",categoria = resultado, producto = productos_resultado)
    else:
        return redirect("/")

#ruta para crear la categoria
@web_app.route("/crearCategoria/<origen>")
#la variable origen hace referencia desde donde se llamó esta ruta 
def crearCategoria(origen):
    #se verifica si la sesion está iniciada
    if session.get("login") == True:
        #trae todas las categorias de esa empresa para mostrar que categorias ya creó
        resultado = mi_categoria.buscarCategorias()

        #redirigir a crear empresa si el usuario no tiene
        if resultado == "no tiene empresa":
            return redirect("/crearEmpresa")

        #se renderiza el html de crear categoria con las categorias de la empresa y se envia la variable de origen
        return render_template("crear_categoria.html", categorias = resultado, origen_crear = origen)
    else:
        return redirect("/")

#ruta para comprobar la creacion de la categoria
@web_app.route("/comprobarCrearCategoria/<origen>" , methods=["POST"])
#la variable origen hace referencia desde donde se llamó esta ruta 
def comprobarCrearCategoria(origen):

    #se recolecta los datos
    nombre_categoria = request.form["nombre_categoria"].lower()

    #se sanitiza los campos de categorias 
    resultado = mi_categoria.sanitizacionCamposCategorias(nombre_categoria)

    #condicional para verificar errores en la sanitizacion de los campos de categorias
    if resultado == "campos correctos":

        #metodo para crear la categoria
        respuesta = mi_categoria.crearCategoria(nombre_categoria)

        #redirigir a crear empresa si el usuario no tiene
        if respuesta == "no tiene empresa":
            return redirect("/crearEmpresa")

        #condicional que verifica errores en la creacion de la categoria
        if respuesta == "categoria ya existe":
            #renderiza el html de crear categorias de nuevo con los errores
            return render_template("crear_categoria.html", msg = respuesta)
        else:
            #dependiendo del origen desde donde se llamó la ruta, e dirije de nuevo allá
            if origen == "producto":
                return redirect("/crearProducto")
            else:
                return redirect("/categorias")
    else:
        return render_template("crear_categoria.html", msg = resultado)


#ruta para renderizar hrml para editar categoria
@web_app.route("/editarCategoria/<id>")
def editarCategoria(id):
    #verifica que la sesion esté iniciada
    if session.get("login") == True:
        #busca la categoria que va a editar para colocar los datos en el html
        resultado = mi_categoria.buscarCategoriaPorID(id)

        numero_identidad = session.get("numero_identidad")
        
        resultado_nit = mi_empresa.buscarEmpresaPorNumeroIdentidad(numero_identidad)

        if resultado_nit != resultado[0][1]:
            return redirect("/cerrarSesion")
        else:
            #renderiza el html de editar categoria con los datos que tenia
            return render_template("editar_categoria.html", id_categoria = id, nombre_categoria = resultado[0][2])
    else:
        return redirect("/")

#ruta para comprobar la edicion de la categoria
@web_app.route("/comprobarEditarCategoria/<id>", methods = ["POST"])
def comprobarEditarCategoria(id):
    #recoleccion de datos
    nombre_categoria = request.form["nombre_categoria"]

    #se recolecta la categoria antes de editarla para verificar que si haya cambipos
    resultado = mi_categoria.buscarCategoriaPorID(id)

    #se sanitiza los datos
    resultado_sanitizacion = mi_categoria.sanitizacionCamposCategorias(nombre_categoria)

    #condicional que verifica errores en la sanitizacion de los datos
    if resultado_sanitizacion== "campos correctos":

        #condicional que verifica que si haya cambios en la edicion de la categoria
        if resultado[0][2] == nombre_categoria:
            return render_template("editar_categoria.html", id_categoria = id, nombre_categoria = nombre_categoria, msg = "estas usando el mismo nombre de categoria")

        else:
            #llama metodo para editar la categoria
            resultado = mi_categoria.editarCategoria(id,nombre_categoria)

            #redirigir a crear empresa si el usuario no tiene
            if resultado == "no tiene empresa":
                return redirect("/crearEmpresa")

            #verifica errores a la hora de editar la categoria
            if resultado == "categoria editada":
                return redirect("/categorias")
            
            else:
                return render_template("editar_categoria.html", id_categoria = id, nombre_categoria = nombre_categoria, msg = resultado)
    else:
        return render_template("editar_categoria.html", id_categoria = id, nombre_categoria = nombre_categoria, msg = resultado_sanitizacion)