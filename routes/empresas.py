from flask import send_from_directory
from conexion import *
from models.empresas import *

@web_app.route("/crearEmpresa")
def crearEmpresa():

    #valida si el usuario ha iniciado sesion antes de poder acceder a la ruta
    if session.get("login") != True:
        return redirect("/")
    else:
        return render_template("crear_empresa.html")
    
@web_app.route("/comprobarEmpresa", methods=["POST"])
def comprobarEmpresa():

    #recoleccion de datos desde el html
    nit_empresa = request.form["nit_empresa"]
    nombre_empresa = request.form["nombre_empresa"]
    correo_empresa = request.form["correo_empresa"]
    pais = request.form["pais"]
    ciudad = request.form["ciudad"]
    direccion = request.form["direccion"]
    telefono = request.form["telefono"]
    logo_empresa = request.files["logo_empresa"]

    #sanitizacion a los datos recolectados anteriormente
    datos = mi_empresa.sanitizacionCamposEmpresas(nit_empresa,nombre_empresa,correo_empresa,pais,ciudad,direccion,telefono)

    #validacion si los campos son validos
    if datos == "campos correctos":
        numero_identidad = session.get("numero_identidad")

        #metodo para agregar la empresa con los datos ya sanitizados y si cumplen con el tamaño solicitado
        resultados = mi_empresa.agregarEmpresa(nit_empresa,numero_identidad,nombre_empresa ,correo_empresa,pais,ciudad,direccion,telefono,logo_empresa)

        #validacion de si la empresa ya existe o no
        if resultados == "empresa ya existe":
            return render_template("crear_empresa.html", msg = resultados)
        else:
            return redirect("/inicio")
        
    else: 
        return render_template("crear_empresa.html", msg = datos)

@web_app.route("/empresa")
def miEmpresa():
    #se verifica si hay usuario logueado
    if session.get("login") != True:
        return redirect("/")
    else:
        #se busca el nit de la empresa con el numero de identidad de el usuario logueado
        numero_identidad = session.get("numero_identidad")
        nit_empresa = mi_empresa.buscarEmpresaPorNumeroIdentidad(numero_identidad)

        #se valida si tiene empresa para mandarlo a crear en caso de que no
        if nit_empresa == "no tiene empresa":
            return redirect("/crearEmpresa")
        else:
            #se busca todos los datos de la empresa con el nit
            resultado = mi_empresa.buscarEmpresaPorNit(nit_empresa)

            #se renderiza el html con los datos de la empresa
            return render_template("mi_empresa.html", empresa = resultado)

@web_app.route("/editarEmpresa/<nit>")
def editarEmpresa(nit):

    #verifica que se haya iniciado sesion
    if session.get("login") != True:
        return redirect("/")
    else:
        
        #metodo para buscar la empresa por su nit
        resultado=mi_empresa.buscarEmpresaPorNit(nit)

        #recolecta el numero de identidad de la variable de sesion
        numero_identidad = session.get("numero_identidad")

        #valida si la empresa que se quiere modificar sea la del usuario logueado
        if numero_identidad == resultado[0][1]:
            return render_template("editar_empresa.html",empresa = resultado)
        else:
            return redirect("/cerrarSesion")
        
@web_app.route("/comprobarEditarEmpresa/<nit>", methods=["POST"])
def comprobarEditarEmpresa(nit):

    #recoleccion de datos desde el html
    nit_empresa = request.form["nit_empresa"]
    nombre_empresa = request.form["nombre_empresa"]
    correo_empresa = request.form["correo_empresa"]
    pais = request.form["pais"]
    ciudad = request.form["ciudad"]
    direccion = request.form["direccion"]
    telefono = request.form["telefono"]
    logo_empresa = request.files["logo_empresa"]

    #sanitizacion a los datos recolectados anteriormente
    datos=mi_empresa.sanitizacionCamposEmpresas(nit_empresa,nombre_empresa,correo_empresa,pais,ciudad,direccion,telefono)

    resultado_mi_empresa=mi_empresa.buscarEmpresaPorNit(nit)
     #validacion si los campos son validos
    if datos == "campos correctos":
        numero_identidad = session.get("numero_identidad")

        if logo_empresa.filename == "":
            logo_empresa = "ninguno"
            
        #metodo para editar la empresa con los datos ya sanitizados y si cumplen con el tamaño solicitado
        resultados = mi_empresa.editarEmpresa(nit_empresa,numero_identidad,nombre_empresa ,correo_empresa,pais,ciudad,direccion,telefono,logo_empresa)

        #validacion de si la empresa ya existe o no
        if resultados == "nit cambiado":
            
            return render_template("editar_empresa.html", msg = resultados,empresa=resultado_mi_empresa)
        else:
            return redirect("/empresa")
        
    else: 
        return render_template("editar_empresa.html", msg = datos,empresa=resultado_mi_empresa)

@web_app.route("/uploads/<nombre>")
def uploads(nombre):
    return send_from_directory(web_app.config['CARPETAU'],nombre)


@web_app.route("/verificarNitEmpresa/<id>", methods=["GET"])
def verificarNitEmpresa(id):
    sql = f"SELECT nit_empresa FROM empresas WHERE nit_empresa = '{id}'"
    mi_cursor = base_datos.cursor()
    mi_cursor.execute(sql)
    resultado = mi_cursor.fetchall()
    mi_cursor.close()

    if len(resultado) == 0:
        return jsonify({"mensaje":"si"})
    else:
        return jsonify({"mensaje":"empresa ya existe"})