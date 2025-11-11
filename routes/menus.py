from conexion import *
from models.menus import *
from models.empresas import *
from models.categorias import * 
from models.productos import *
from models.usuarios import *

#ruta para renderizar html para visualizar los menus creados
@web_app.route("/misMenus")
def misMenus():
    if session.get("login") != True:
        redirect("/")
    else:
        numero_identidad = session.get("numero_identidad")
        empresa = mi_empresa.buscarEmpresaPorNumeroIdentidad(numero_identidad)

        if empresa == "no tiene empresa":
            return redirect("/")
        else:
            menus = mi_menu.buscarMenus(empresa)
            asignado = mi_menu.menuAsignado(empresa)
            return render_template("mis_menus.html",contador_menus = len(menus), mis_menus = menus, asignado = asignado)

#ruta para renderizar el html de agregar menú
@web_app.route("/agregarMenu")
def agregarMenu():
    if session.get("login") != True:
        redirect("/")
    else: 
        return render_template("crear_menu.html")

@web_app.route("/comprobarAgregarMenu", methods = ["POST"])
def comprobarAgregarMenu():
    #recoleccion de datos
    nombre = request.form["nombre"]

    #sanitizacion de los campos 
    resultado_sanitizacion =mi_menu.sanitizacionCamposMenu(nombre)

    #verificar la sanitizacion
    if resultado_sanitizacion != "campos correctos":
        return render_template("crear_menu.html")
    else:
        #recolectar el numero de identidad del usuario logueado
        numero_identidad = session.get("numero_identidad")

        #buscar el nit de la empresa del usuario logueado
        empresa = mi_empresa.buscarEmpresaPorNumeroIdentidad(numero_identidad)

        #verificar con el resultado anterior si el usuario tiene empresa creada
        if empresa == "no tiene empresa":
            return redirect("/crearEmpresa")
        else:
            resultado_crear = mi_menu.crearMenu(nombre,empresa)

            if resultado_crear == "este nombre ya existe en tus menus":
                return render_template("crear_menu.html")
            else:
                return redirect("/misMenus")

@web_app.route("/editarNombreMenu/<id>")
def editarNombreMenu(id):
    if session.get("login") != True:
        return redirect("/")
    else:
        numero_identidad = session.get("numero_identidad") 
        empresa = mi_empresa.buscarEmpresaPorNumeroIdentidad(numero_identidad)

        if empresa == "no tiene empresa":
            return redirect("/crearEmpresa")
        else:
            menu = mi_menu.buscarMenuUnico(empresa,id)

            if menu == "menu no existe":
                return redirect("/cerrarSesion")
            else:
                return render_template("editar_nombre_menu.html",id = id, menus = menu )

@web_app.route("/comprobarEditarNombreMenu/<id>", methods=["POST"])
def comprobarEditarNombreMenu(id):
    nombre = request.form["nombre"]

    resultado_sanitizacion = mi_menu.sanitizacionCamposMenu(nombre)
    numero_identidad = session.get("numero_identidad")

    empresa = mi_empresa.buscarEmpresaPorNumeroIdentidad(numero_identidad)

    if resultado_sanitizacion != "campos correctos":
         
        
        if empresa == "no tiene empresa":
            return redirect("/crearEmpresa")
        else:
            menu = mi_menu.buscarMenuUnico(empresa,id)

            if menu == "menu no existe":
                return redirect("/cerrarSesion")
            else:
                return render_template("editar_nombre_menu.html",id = id, menus = menu, msg = resultado_sanitizacion)
    else:

        if empresa == "no tiene empresa":
            return redirect("/crearEmpresa")
        else:
            menu = mi_menu.buscarMenuUnico(empresa, id)

            if len(menu) == 0:
                return redirect("/cerrarSesion")
            else:
                if menu[0][1] == nombre:
                    return render_template("editar_nombre_menu.html",id = id, menus = menu, msg = "No se ha modificado el nombre del menú")
                else:
                    resultado_editar = mi_menu.editarMenu(nombre,empresa,id)

                    if resultado_editar == "este nombre ya existe en tus menus":
                        return render_template("editar_nombre_menu.html",id = id, menus = menu, msg = resultado_editar)
                    else:
                        return redirect("/misMenus")
                
@web_app.route("/categoriasMenu/<id>")
def categoriasMenú(id):
    if session.get("login") != True:
        return redirect("/")
    else:
        numero_identidad = session.get("numero_identidad")
        empresa = mi_empresa.buscarEmpresaPorNumeroIdentidad(numero_identidad )

        if empresa == "no tiene empresa":
            return redirect("/crearEmpresa")
        else:
            producto = mi_producto.buscarProductosConCategoria()
            categoria = mi_menu.buscarCategoriasMenu(id)
            menu = mi_menu.buscarMenuUnico(empresa,id)

            print(menu)
            
            if menu != "menu no existe" :
                return render_template("categorias_menu.html", id = id, menu = menu, categoria = categoria, producto = producto)
            else:
                return redirect("/cerrarSesion")

@web_app.route("/asignarCategoriasMenu/<id>")
def asignarCategoriasMenu(id):
    if session.get("login") != True:
        return redirect("/")
    else:
        seleccionados = mi_menu.categoriasMenu(id)
        categorias = mi_categoria.buscarCategorias()

        if categorias == "no tiene empresa":
            return redirect("/crearEmpresa")
        else:
            numero_identidad = session.get("numero_identidad")
            empresa = mi_empresa.buscarEmpresaPorNumeroIdentidad(numero_identidad)
            menu = mi_menu.buscarMenuUnico(empresa,id)

            if len(menu) == 0:
                return redirect("/cerrarSesion")
            else:
                return render_template("asignar_categorias_menus.html",resul = categorias, seleccionados = seleccionados, id = id, nombre_menu = menu[0][1] )


@web_app.route("/comprobarAsignarCategoriasMenu/<id>",methods=["POST"])
def comprobarAsignarCategoriasMenu(id):
    seleccionadas = request.form.getlist("seleccionadas")
    #no olvidar sanitizacion
    resultado_sanitizacion = mi_producto.sanitizarCategoriasSeleccionadas(seleccionadas)

    resultado_seleccionadas = mi_menu.categoriasMenu(id)
    resultado = mi_categoria.buscarCategorias()
    #validar errores en la sanitizacion de los id de las categorias
    if resultado_sanitizacion == "categoria invalida":
        
        return render_template("asignar_categorias_menus.html", resul = resultado,seleccionados = resultado_seleccionadas, id = id)
    else:
        resultado_asignacion = mi_menu.asignarCategorias(seleccionadas, id)

        if resultado_asignacion == "asignadas":
            return redirect(f"/categoriasMenu/{id}")
        else:
            return render_template("asignar_categorias_menus.html", resul = resultado,seleccionados = resultado_seleccionadas, id = id)


@web_app.route("/eliminarMenu/<id>")
def eliminarMenu(id):
    if session.get("login") != True:
        return redirect("/")
    else:
        resultado = mi_menu.eliminarMenu(id)
        
        if resultado == "no tiene empresa":
            return redirect("/crearEmpresa")
        elif resultado == "no":
            return redirect("/cerrarSesion")
        else:
            return redirect("/misMenus")

@web_app.route("/traerMenus", methods = ["GET"])
def traerMenus():
    numero_identidad = session.get("numero_identidad")
    empresa = mi_empresa.buscarEmpresaPorNumeroIdentidad(numero_identidad)
    menus = mi_menu.buscarMenus(empresa)

    return jsonify({"menus": menus})

@web_app.route("/asignarMenu", methods = ["POST"])
def asignarMenu():
    id_menu = request.form["asigna_menu"]
    
    numero_identidad = session.get("numero_identidad")
    empresa = mi_empresa.buscarEmpresaPorNumeroIdentidad(numero_identidad)

    if empresa == "no tiene empresa":
        return redirect("/crearEmpresa")
    else:
        mi_menu.asignarMenu(id_menu,empresa)

        return redirect("/inicio")
    

@web_app.route("/ordenarCategorias/<id>")
def ordenarCategorias(id):
    if session.get("login") != True:
        return redirect("/")
    else:
        numero_identidad = session.get("numero_identidad")
        empresa = mi_empresa.buscarEmpresaPorNumeroIdentidad(numero_identidad )

        if empresa == "no tiene empresa":
            return redirect("/crearEmpresa")
        else:

            categoria = mi_menu.buscarCategoriasMenu(id)
            menu = mi_menu.buscarMenuUnico(empresa,id)

            print(menu)
            
            if menu != "menu no existe" :
                return render_template("ordenar_categorias.html", id = id, menu = menu, categoria = categoria)
            else:
                return redirect("/cerrarSesion")