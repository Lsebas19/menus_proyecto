from conexion import *
from models.usuarios import *

#ruta principal que renderiza el html de inicio de sesion
@web_app.route("/")
def iniciarSesion():
    if session.get("login") == True:
        return redirect("/inicio")
    else:
        return render_template("index.html")

#ruta para recolectar datos de inicio de sesion y validarlos
@web_app.route("/comprobarIniciar", methods = ["POST"])
def comprobarInicioSesion():
    
    #recoleccion de datos de inicio de sesion
    numero_identidad = request.form["numero_identidad"]
    contrasena = request.form["contrasena"]
    
    #sanitizacion de campos para evitar enviar datos basura
    datos = mi_usuario.sanitizacionCampo(numero_identidad,contrasena)

    if datos == "campos correctos":
        #asignacion de datos sanitizados a las variables anteriores
        #comprobacion de la los datos para saber si el usuario existe
        resultado = mi_usuario.comprobarUsuario(numero_identidad, contrasena)

        #validacion para saber si se encontró el usuario
        if resultado == "no encontrado":
            return render_template("index.html", msg = "credenciales incorrectas")
        
        elif resultado == "administrador":
            session["login"] = True
            session["numero_identidad"] = numero_identidad
            session["rol"] = 1
            return redirect("/inicioAdmin")
        
        else:
            session["login"] = True
            session["rol"] = 0
            session["numero_identidad"] = numero_identidad
            #recolectar el resultado de la busqueda de empresa del usuario
            resultado_empresa = mi_usuario.comprobarEmpresa(numero_identidad)
            
            #validar el dato de resultado_empresa
            if resultado_empresa == "no tiene empresa":
                return redirect("/crearEmpresa")
            else:
                return redirect("/inicio")
    else:
        return render_template("index.html", msg = datos)


#ruta para la generar el html para crear usuario
@web_app.route("/crearUsuario")
def crearUsuario():
    #verifica si hay sesion iniciada
    if session.get("login") != True:
        return redirect("/")
    else:
        #renderiza el html para crear usuario 
        return render_template("crear_usuario.html")


#ruta para crear usuario
@web_app.route("/comprobarCrearUsuario", methods=["POST"])
def comprobarCreacionUsuario():

    #recoleccion de los datos
    numero_identidad = request.form["numero_identidad"]
    nombre = request.form["nombre"]
    correo = request.form["correo"]
    contrasena = request.form["contrasena"]

    #sanitizacion de los datos
    resultado = mi_usuario.sanitizacionCrearUsuario(numero_identidad, nombre,correo,contrasena)

    #condicional para verificar errores en la sanitizacion
    if resultado == "campos correctos":
        #metodo para la creacion del usuario
        resultado_crear_usuario = mi_usuario.crearUsuario(numero_identidad,nombre,correo,contrasena)

        #condicional para verificar errores en la creacion del usuario 
        if resultado_crear_usuario == "usuario ya existe":
           #renderizar el html con el error
           return render_template("crear_usuario.html", msg = resultado_crear_usuario)
        else:
            #redireccionar a inicio de administrador al crear el usuario
            return redirect("/inicioAdmin")
    else:
        #renderizar el html con el error
        return render_template("crear_usuario.html", msg = resultado)
    

#ruta para acceder al inicio del cliente
@web_app.route("/inicio")
def inicio():
    #verifica si hay sesion iniciada
    if session.get("login") != True:
        #en caso tal de que no, redirije a iniciar sesion
        return redirect("/")
    else:
        #si si la hay se renderiza el html de inicio
        return render_template("inicio.html")
    

@web_app.route("/cerrarSesion")
def cerrarSesion():

    #la variable de sesion de login la cambia a falsa para que tenga que iniciar sesion de nuevo
    session["login"] = False
    return redirect("/")

#ruta para acceder al inicio del administrador
@web_app.route("/inicioAdmin")
def inicioAdmin():
    #verifica si hay sesion iniciada
    if session.get("login") != True:
        #en caso tal de que no, redirije a iniciar sesion
        return redirect("/")
    else:
        id = session.get("numero_identidad")
        usuario = mi_usuario.buscarUsuarioPorID(id)

        if usuario[0][6] == 1:
            resultado = mi_usuario.buscarUsuarios()
            #si si la hay se renderiza el html de inicio
            return render_template("inicio_admin.html", usuarios = resultado, nombre = usuario[0][1])
        else:
            return redirect("/cerrarSesion")

@web_app.route("/usuario")
def miUsuario():
    if session.get("login") != True:
        return redirect("/")
    else:
        numero_identidad = session.get("numero_identidad")
        resultado = mi_usuario.buscarUsuarioPorID(numero_identidad)

        return render_template("mi_usuario.html",usuario=resultado)

@web_app.route("/editarUsuario/<id>")
def editarUsuario(id):
    #verifica que se haya iniciado sesion
    if session.get("login") != True:
        return redirect("/")
    else:
        if session.get("rol") == 1:
            resultado = mi_usuario.buscarUsuarioPorID(id)
            return render_template("editar_usuario.html",usuario=resultado)
        else:
            return redirect("/")
    
@web_app.route("/comprobarEditarUsuario",methods=["POST"])
def comprobarEditarUsuario():
    #recoleccion de los datos
    numero_identidad = request.form["numero_identidad"]
    nombre = request.form["nombre"]
    correo = request.form["correo"]

    #sanitizacion de los datos
    resultado = mi_usuario.sanitizacionEditarUsuario(numero_identidad, nombre,correo)
    
    #condicional para verificar errores en la sanitizacion
    if resultado == "campos correctos":
        #metodo para la edicion del usuario
        
        mi_usuario.editarUsuario(numero_identidad,nombre,correo)
        #redireccionar a usuario
        return redirect("/inicioAdmin")
    else:
        #renderizar el html con el error
        return render_template("editar_usuario.html", msg = resultado)

@web_app.route("/cambiarContrasena")
def cambiarContrasena():
    if session.get("login") != True:
        return redirect("/")
    else:
        #recolecta el numero de identidad del usuario logueado para buscar los datos de este
        return render_template("cambiar_contrasena.html")

@web_app.route("/comprobarCambioContrasena", methods=["POST"])
def comprobarCambioContrasena():
    #recoleccion de datos
    contrasena_vieja = request.form["contrasena_vieja"]
    contrasena_nueva = request.form["contrasena_nueva"]

    #sanitizacion de las contraseñas
    resultado = mi_usuario.sanitizacionContrasenas(contrasena_vieja,contrasena_nueva)

    #verificacion de errores en la sanitizacion
    if resultado != "campos correctos":
        return render_template("cambiar_contrasena.html",msg=resultado)
    else:
        #buscar la contraseña vieja del usuario para comparar
        id = session.get("numero_identidad")
        resultado_usuario = mi_usuario.buscarUsuarioPorID(id)

        #se cifra la contraseña para comparar
        resultado = mi_usuario.cifrarContrasena(contrasena_vieja)

        #se verifica si las contraseñas coinciden
        if resultado != resultado_usuario[0][3]:
            return render_template("cambiar_contrasena.html",msg="contraseña incorrecta")
        else:
            mi_usuario.cambiarContrasena(id,contrasena_nueva)
            return redirect("/usuario")

@web_app.route("/verificarNumeroIdentidad/<id>", methods=["GET"])
def verificarNumeroIdentidad(id):
    sql = f"SELECT numero_identidad FROM usuarios WHERE numero_identidad = '{id}'"
    mi_cursor = base_datos.cursor()
    mi_cursor.execute(sql)
    resultado = mi_cursor.fetchall()
    mi_cursor.close()

    if len(resultado) == 0:
        return jsonify({"mensaje":"si"})
    else:
        return jsonify({"mensaje":"usuario ya existe"})

@web_app.route("/eliminarUsuario/<id>")
def eliminarUsuario(id):
    if session.get("login") != True:
        return redirect("/")
    else:
        if session.get("rol") != 1:
            return redirect("/cerrarSesion")
        else:
            mi_usuario.eliminarUsuario(id)
            return redirect("/inicioAdmin")