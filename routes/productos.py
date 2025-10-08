from conexion import *
from models.categorias import * 
from models.productos import *

#ruta para mostrar los productos de la empresa 
@web_app.route("/productos")
def productos():
    #verifica que la sesion esté iniciada
    if session.get("login") == True:
        #metodo para buscar los productos de la empresa 
        productos_resultado=mi_producto.buscarProductos()

        #redirigir a crear empresa si el usuario no tiene
        if productos_resultado == "no tiene empresa":
            return redirect("/crearEmpresa")

        #renderiza el html con los productos recolectados
        return render_template("productos.html", producto = productos_resultado)
    else:
        return redirect("/")

#ruta para renderizar html de crear producto
@web_app.route("/crearProducto")
def crearProductos():
    #verifica que la sesion esté iniciada
    if session.get("login") == True:

        #busca las categorias de la empresa 
        resultado = mi_categoria.buscarCategorias()

        #redirigir a crear empresa si el usuario no tiene
        if resultado == "no tiene empresa":
            return redirect("/crearEmpresa")

        #busca los productos de la empresa 
        resultado_productos = mi_producto.buscarProductos()

        #renderiza el html con los datos recolectados 
        return render_template("crear_productos.html", categorias = resultado, productos = resultado_productos)
    else:
        return redirect("/")

#ruta para comprobar la creacion del producto
@web_app.route("/crearProductoComprobar", methods=["POST"])
def crearProductoComprobar():

    #recoleccion de datos
    categoria = request.form["categoria"]
    nombre_producto = request.form["nombre_producto"].lower()
    descripcion_producto = request.form["descripcion_producto"].lower()
    presentacion_producto = request.form["presentacion_producto"].lower()
    imagen_producto = request.files["imagen_producto"]
    precio_producto = request.form["precio_producto"]
    
    #sanitizacion del id de la categoria 
    resultado_categoriaS = mi_categoria.sanitizarIdCategoria(categoria)

    #buscar las categorias de la empresa 
    resultado_categoria = mi_categoria.buscarCategorias()

    #redirigir a crear empresa si el usuario no tiene
    if resultado_categoria == "no tiene empresa":
        return redirect("/crearEmpresa")

    #buscar los productos de la empresa
    resultado_productos = mi_producto.buscarProductos()

    #condicional que verifica los errores en la sanitizacion del id de categoria 
    if resultado_categoriaS == "campos correctos":

        #sanitizacion de los datos del producto
        resultado = mi_producto.santiziacionCamposProductos(nombre_producto,descripcion_producto,presentacion_producto,precio_producto)

        #condicional que verifica errores en la santizacion de datos
        if resultado == "campos correctos":

            #metodo de creacion del producto
            resultado = mi_producto.crearProducto(categoria,nombre_producto,descripcion_producto,presentacion_producto,imagen_producto,precio_producto)

            #condicional para validar errores de la creacion del producto
            if resultado == "producto ya existe":
                #renderizar el html con los errores
                return render_template("crear_productos.html", msg = resultado, categorias = resultado_categoria, productos = resultado_productos)
            else:
                #redirije a la ruta productos al crearlo
                return redirect("/productos")
        else:
            return render_template("crear_productos.html", msg= resultado, categorias = resultado_categoria, productos = resultado_productos)
    else:
        return render_template("crear_productos.html", msg= resultado_categoriaS, categorias = resultado_categoria, productos = resultado_productos)

#ruta para renderizar html de editar productos
@web_app.route("/editarProducto/<id>")
def editarProducto(id):
    #verifica que haya sesion iniciada    
    if session.get("login") == True:
        #recolecta los datos del producto que se va a editar
        resultado_producto = mi_producto.buscarProductoPorID(id)

        #busca el numero de identidad del usuario logueado
        numero_identidad = session.get("numero_identidad")
        
        #busca el nit de la empresa del usuario logueado
        resultado_nit = mi_empresa.buscarEmpresaPorNumeroIdentidad(numero_identidad)

        #compara el nit del usuario logueado con el del producto para saber si se edita el producto de esa empresa
        if resultado_nit != resultado_producto[0][7]:
            return redirect("/cerrarSesion")
        else:

        #buscar todos los productos de la empresa para mostrar cuales ya han sido creados
            resultado_buscar = mi_producto.buscarProductos()

            #redirigir a crear empresa si el usuario no tiene
            if resultado_buscar == "no tiene empresa":
                return redirect("/crearEmpresa")
            
            #renderizar el html de editar producto
            return render_template("editar_producto.html", resultado = resultado_producto, productos = resultado_buscar, id_producto = id)
    else:
        return redirect("/")
    
#ruta para editar producto
@web_app.route("/editarProductoComprobar/<id>",methods=["POST"])
def editarProductoComprobar(id):

    #recoleccion de datos
    nombre_producto = request.form["nombre_producto"].lower()
    descripcion_producto = request.form["descripcion_producto"].lower()
    presentacion_producto = request.form["presentacion_producto"].lower()
    imagen_producto = request.files["imagen_producto"]
    precio_producto = request.form["precio_producto"]
    
    #buscar el producto a modificar 
    resultado_buscar_producto = mi_producto.buscarProductoPorID(id)

    #buscar los productos 
    resultado_buscar = mi_producto.buscarProductos()

    #redirigir a crear empresa si el usuario no tiene
    if resultado_buscar == "no tiene empresa":
        return redirect("/crearEmpresa")

    #verifica que se haya modificado algo del producto
    if resultado_buscar_producto[0][1] == nombre_producto and resultado_buscar_producto[0][2] == descripcion_producto and resultado_buscar_producto[0][3] == presentacion_producto and resultado_buscar_producto[0][5] == precio_producto:

        #si no se mofica nada se manda  el mensaje de que no se a modificado nada 
        return render_template("editar_producto.html", resultado = resultado_buscar_producto, productos = resultado_buscar, id_producto = id, msg = "no se ha modificado nada")
    
    else:
        #sanitizacion de los datos del producto
        resultado_sanitizacion = mi_producto.santiziacionCamposProductos(nombre_producto,descripcion_producto,presentacion_producto,precio_producto)

        #condicional que verifica los errores en la santizacion de los datos
        if resultado_sanitizacion == "campos correctos":
            
            #metodo que edita el producto
            resultado_editar = mi_producto.editarProducto(id,nombre_producto,descripcion_producto,presentacion_producto,imagen_producto,precio_producto)

            #verifica errores en la edicion del producto
            if resultado_editar == "producto editado":
                #redirije a productos 
                return redirect("/productos")
            else:
                #renderiza html de nuevo con los errores
                return render_template("editar_producto.html", resultado = resultado_buscar_producto, productos = resultado_buscar, id_producto = id, msg = resultado_editar)

        else:
            return render_template("editar_producto.html", resultado = resultado_buscar_producto, productos = resultado_buscar, id_producto = id, msg = resultado_sanitizacion)

#ruta para eliminar el producto
@web_app.route("/eliminarProducto/<id>")
def eliminarProducto(id):
    #verifica que la sesion este iniciada
    if session.get("login") == True:
        #metodo que elimina el producto 
        resultado = mi_producto.eliminarProducto(id)

        #condicional que verifica si se eliminó el producto
        if resultado == "producto eliminado":
            return redirect("/productos")
    else:
        return redirect("/")

@web_app.route("/asignarCategoria/<id>")
def asignarCategoria(id):
    if session.get("login") == True:
        #recolecta los datos del producto que se va a editar
        resultado_producto = mi_producto.buscarProductoPorID(id)

        #busca el numero de identidad del usuario logueado
        numero_identidad = session.get("numero_identidad")
        
        #busca el nit de la empresa del usuario logueado
        resultado_nit = mi_empresa.buscarEmpresaPorNumeroIdentidad(numero_identidad)

        #compara el nit del usuario logueado con el del producto para saber si se edita el producto de esa empresa
        if resultado_nit != resultado_producto[0][7]:
            return redirect("/cerrarSesion")
        else:
            resultado_seleccionadas = mi_producto.categoriasProducto(id)
            resultado = mi_categoria.buscarCategorias()
            return render_template("asignar_categorias.html", resul = resultado,seleccionados = resultado_seleccionadas, id = id)
    else:
        return redirect("/")

@web_app.route("/comprobarAsignarCategorias/<id>",methods=["POST"])
def comprobarAsignarCategorias(id):
    seleccionadas = request.form.getlist("seleccionadas")
    #no olvidar sanitizacion
    resultado_sanitizacion = mi_producto.sanitizarCategoriasSeleccionadas(seleccionadas)

    resultado_seleccionadas = mi_producto.categoriasProducto(id)
    resultado = mi_categoria.buscarCategorias()
    #validar errores en la sanitizacion de los id de las categorias
    if resultado_sanitizacion == "categoria invalida":
        
        return render_template("asignar_categorias.html", resul = resultado,seleccionados = resultado_seleccionadas, id = id, msg = resultado_sanitizacion)
    else:
        resultado_asignacion = mi_producto.asignarCategorias(seleccionadas, id)

        if resultado_asignacion == "asignadas":
            return redirect("/productos")
        else:
            return render_template("asignar_categorias.html", resul = resultado,seleccionados = resultado_seleccionadas, id = id, msg = resultado_asignacion)





