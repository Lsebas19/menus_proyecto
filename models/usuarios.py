from conexion import *
import hashlib
import re



class Usuario:
    def comprobarUsuario(self, numero_identidad, contrasena):

        #llamar el metodo para cifrar la contraseña
        contrasena_cifrada = mi_usuario.cifrarContrasena(contrasena)

        #instruccion sql para encontrar usuario con el numero de identidad y contraseña digitados
        sql = f"SELECT nombre, rol FROM usuarios WHERE numero_identidad = '{numero_identidad}' AND contrasena = '{contrasena_cifrada}' AND estado = 1"

        mi_cursor = base_datos.cursor()
        #Ejecucion de la sentencia sql
        mi_cursor.execute(sql)

        #recoleccion del nombre del usuario y asignacion a la variable
        nombre = mi_cursor.fetchall()
        mi_cursor.close()
        #condicional para validar si el cursor trajo algun usuario
        if len(nombre) != 1:
            return "no encontrado"
        else: 
            if nombre[0][1] == 1 :
                return "administrador"
            else:
                return "encontrado"

    
    def cifrarContrasena(self, contrasena):
        #cifrado de contraseña
        cifrada = hashlib.sha512(contrasena.encode("utf-8")).hexdigest()
        return cifrada


    def sanitizacionCampo(self, numero_identidad, contrasena):

        #evitar que los campos contengan caracteres no deseados por medio de expresiones regulares
        numero_identidadS = re.sub(r'[^a-zA-Z0-9]', '', numero_identidad)
        contrasenaS = re.sub(r'[^a-zA-Z0-9\#\@\%\\]', '', contrasena)

        #validar si el numero de identidad cumple con el tamaño del dato esperado
        if len(numero_identidad) > 5 and len(numero_identidad) < 16 and numero_identidadS == numero_identidad:
            #validar si la contraseña cumple con el tamaño del dato esperado
            if len(contrasena) > 5 and len(contrasena) < 12 and contrasenaS == contrasena:
                return "campos correctos"
            else:
                return "contraseña invalida"
                
        else:
            return "numero de identidad invalido"
                

    def comprobarEmpresa(self, numero_identidad):
        
        #sentencia sql para saber si el usuario tiene empresa
        sql = f"SELECT nombre FROM empresas WHERE '{numero_identidad}' = numero_identidad AND estado = 1"
        mi_cursor = base_datos.cursor()
        mi_cursor.execute(sql)

        resultado = mi_cursor.fetchall()
        mi_cursor.close()
        #validar si la sentencia encontró empresa de usuario
        if len(resultado) == 1:
            return "tiene empresa"
        else: 
            return "no tiene empresa"

    #metodo para crear usuario
    def crearUsuario(self, numero_identidad, nombre, correo, contrasena):
        
        #sentencia sql para buscar si existe un usuario con ese numero de identidad
        sql = f"SELECT nombre FROM usuarios WHERE '{numero_identidad}' = numero_identidad AND estado = 1"
        mi_cursor = base_datos.cursor()
        mi_cursor.execute(sql)
        resultado = mi_cursor.fetchall()
        mi_cursor.close()
        #condicional para saber si el usuario existe
        if len(resultado) > 0:
            #error
            return "usuario ya existe"
        else:

            #obtiene fecha y hora en la que se creó el usuario
            fecha = datetime.now()
            #llama el metodo que cifra la contraseña
            cifrada = mi_usuario.cifrarContrasena(contrasena)

            #inserta los datos
            sql = f"INSERT INTO usuarios (numero_identidad, nombre, correo, contrasena, fecha_creacion ) VALUES('{numero_identidad}','{nombre}','{correo}','{cifrada}','{fecha}')"
            mi_cursor = base_datos.cursor()
            mi_cursor.execute(sql)

            base_datos.commit()
            mi_cursor.close()
    
    def sanitizacionCrearUsuario(self, numero_identidad,nombre,correo,contrasena):

        #evitar que los campos contengan caracteres no deseados por medio de expresiones regulares
        numero_identidadS = re.sub(r'[^0-9]', '', numero_identidad)
        contrasenaS = re.sub(r'[^a-zA-Z0-9]', '', contrasena)
        nombreS = re.sub(r'[^a-zA-Z0-9\ ]', '', nombre)
        correoS = re.sub(r'[^a-z0-9\.\-\_\@]', '', correo)

        #validar si el numero de identidad cumple con el tamaño del dato esperado
        
        if len(numero_identidad) < 16 and len(numero_identidad) > 5 and numero_identidadS == numero_identidad:
            
            #valida el nombre
            if len(nombre) < 86 and len(nombre) > 0 and  nombreS == nombre:

                #valida el correo
                if len(correo) < 65 and len(correo) > 10 and correoS == correo:
                    
                    #valida la contraseña
                    if len(contrasena) > 5 and len(contrasena) < 13 and contrasenaS == contrasena:
                        return "campos correctos"
                    else:
                        return "contraseña invalida"
                        
                else:
                    return "correo invalido"
                    
            else:
                return "nombre invalido"
                
        else:
            return "numero de identidad invalido"
    

    def sanitizacionEditarUsuario(self, numero_identidad,nombre,correo):

        #evitar que los campos contengan caracteres no deseados por medio de expresiones regulares
        numero_identidadS = re.sub(r'[^0-9]', '', numero_identidad)
        nombreS = re.sub(r'[^a-zA-Z0-9\ ]', '', nombre)
        correoS = re.sub(r'[^a-z0-9\.\-\_\@]', '', correo)

        #validar si el numero de identidad cumple con el tamaño del dato esperado
        
        if len(numero_identidad) < 16 and len(numero_identidad) > 5 and numero_identidadS == numero_identidad:
            
            #valida el nombre
            if len(nombre) < 86 and len(nombre) > 0 and  nombreS == nombre:

                #valida el correo
                if len(correo) < 65 and len(correo) > 10 and correoS == correo:
                    
                    return "campos correctos"
                else:
                    return "correo invalido"
                    
            else:
                return "nombre invalido"
                
        else:
            return "numero de identidad invalido"
    
    #metodo para buscar el nombre de usuario
    def buscarNombreUsuario(self,id):
        sql = f"SELECT nombre FROM usuarios WHERE numero_identidad = '{id}'"  
        mi_cursor = base_datos.cursor()
        mi_cursor.execute(sql)
        nombre = mi_cursor.fetchall()
        mi_cursor.close()
        return nombre
    
    #metodo para buscar usuario por su numero de identidad
    def buscarUsuarioPorID(self,id):
        sql = f"SELECT * FROM usuarios WHERE numero_identidad = '{id}'"
        mi_cursor = base_datos.cursor()
        mi_cursor.execute(sql)
        usuario = mi_cursor.fetchall()
        mi_cursor.close()
        return usuario

    #metodo para crear usuario
    def editarUsuario(self, numero_identidad, nombre, correo):
        
            #obtiene fecha y hora en la que se creó el usuario
        fecha = datetime.now()

        #inserta los datos
        sql = f"UPDATE usuarios SET nombre = '{nombre}',correo='{correo}',fecha_creacion='{fecha}' WHERE numero_identidad = '{numero_identidad}'"
        
        mi_cursor = base_datos.cursor()    
        mi_cursor.execute(sql)

        base_datos.commit()
        mi_cursor.close()

    def sanitizacionContrasenas(self,contrasena_vieja,contrasena_nueva):

        #evitar que los campos contengan caracteres no deseados por medio de expresiones regulares
        contrasenaSVieja = re.sub(r'[^a-zA-Z0-9]', '', contrasena_vieja)

        contrasenaSNueva = re.sub(r'[^a-zA-Z0-9]', '', contrasena_nueva)

        #valida la contraseña
        if len(contrasena_vieja) > 5 and len(contrasena_vieja) < 13 and contrasenaSVieja == contrasena_vieja:
            if len(contrasena_nueva) > 5 and len(contrasena_nueva) < 13 and contrasenaSNueva == contrasena_nueva:
                return "campos correctos"
            else:
                return "contraseña invalida"
        else:
            return "contraseña invalida"
    
    #metodo para actualizar la contraseña
    def cambiarContrasena(self,id, contrasena):

        cifrada = mi_usuario.cifrarContrasena(contrasena)

        sql = f"UPDATE usuarios SET contrasena='{cifrada}' WHERE numero_identidad ='{id}' "
        mi_cursor = base_datos.cursor()
        mi_cursor.execute(sql)

        base_datos.commit()
        mi_cursor.close()
    
    def buscarUsuarios(self):
        sql = f"SELECT * FROM usuarios WHERE rol = 0 AND estado = 1"
        mi_cursor = base_datos.cursor()
        mi_cursor.execute(sql)

        resultado = mi_cursor.fetchall()
        mi_cursor.close()
        
        return resultado

    def eliminarUsuario(self, id):
        sql = f"UPDATE usuarios SET estado = 0 WHERE numero_identidad = '{id}'"
        mi_cursor = base_datos.cursor()
        mi_cursor.execute(sql)

        base_datos.commit()
        mi_cursor.close()
mi_usuario = Usuario()