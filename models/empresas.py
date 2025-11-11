
import hashlib
from conexion import *
import qrcode


class Empresas:

    def sanitizacionCamposEmpresas(self, nit_empresa,nombre_empresa,correo_empresa,pais,ciudad,direccion,telefono):

        #limpiar los datos recibidos para evitar dejar entrar caracteres no permitidos
        nit_empresaS = re.sub(r'[^0-9]', '', nit_empresa)
        nombre_empresaS = re.sub(r'[^a-zA-Z0-9\ ]', '', nombre_empresa)
        correo_empresaS = re.sub(r'[^a-z0-9\.\-\_]+@+[^a-z0-9]+.+[^a-z\.]', '', correo_empresa)
        paisS = re.sub(r'[^a-zA-Z]', '', pais)
        ciudadS= re.sub(r'[^a-zA-Z]', '', ciudad)
        direccionS = re.sub(r'[^a-zA-Z0-9\#\-]', '', direccion)
        telefonoS = re.sub(r'[^0-9]', '', telefono) 

        #validacion del tamaño de los campos y si cumplen con lo estipulado

        #valida el nit de la empresa
        if len(nit_empresa) == 9 and nit_empresaS == nit_empresa:

            #valida el nombre de la empresa
            if len(nombre_empresa) > 3 and len(nombre_empresa) < 85 and nombre_empresa == nombre_empresaS:

                #valida el correo de la empresa
                if len(correo_empresa) > 10 and len(correo_empresa) < 65 and correo_empresa == correo_empresaS:

                    #valida la ciudad
                    if len(ciudad) > 0 and len(ciudad) < 59 and ciudad == ciudadS:
                        
                        #valida la direccion
                        if len(direccion) > 2 and len(direccion) < 169 and direccion == direccionS:
                            
                            #valida el telefono
                            if len(telefono) == 10 and telefono == telefonoS: 

                                return "campos correctos"
                            
                            else:
                                return "telefono invalido"
                                
                        else:
                            return "direccion invalida"
                            
                    else:
                        return "ciudad invalida"
                        
                else:
                    return "correo invalido"
                    
            else:
                return "nombre invalido"
                
        else: 
            return "nit invalido"
            



    def agregarEmpresa(self, nit_empresa,numero_identidad,nombre_empresa,correo_empresa,pais,ciudad,direccion,telefono,logo):

        #sentencia sql para buscar una empresa que tenga el mismo nit digitado
        sql = f"SELECT nit_empresa FROM empresas WHERE '{nit_empresa}' = nit_empresa AND estado = 1"
        mi_cursor = base_datos.cursor()
        mi_cursor.execute(sql)
        resultado = mi_cursor.fetchall()
        mi_cursor.close()

        #validar si la empresa existe 
        if len(resultado) == 1:
            return "empresa ya existe"

        else:

            #llamar metodo para generar el link que usara la empresa para visualizar el menu
            link = mi_empresa.generarLink(nit_empresa)

            qr = mi_empresa.generarQr(link)

            cifrado = hashlib.sha512(nit_empresa.encode("utf-8")).hexdigest()
            #variable donde se guarda la fecha y hora actual en la que se añade la empresa
            fecha_creacion = datetime.now()

            if logo != "ninguno":
                logo = mi_empresa.guardarFoto(logo)

            #sentencia sql para agregar la empresa
            sql = f"INSERT INTO empresas(nit_empresa,numero_identidad,nombre,correo,ciudad,codigo_qr,link,direccion,telefono,pais,logo,fecha_creacion,cifrado) VALUES('{nit_empresa}','{numero_identidad}','{nombre_empresa}','{correo_empresa}','{ciudad}','{qr}','{link}','{direccion}','{telefono}','{pais}','{logo}','{fecha_creacion}','{cifrado}')"

            mi_cursor = base_datos.cursor()
            mi_cursor.execute(sql)

            base_datos.commit()
            mi_cursor.close()
            return "empresa creada"


    #metodo para generar el link de visualizacion del menú
    def generarLink(self,nit_empresa):

        #cifrado de el nit ya que este se utilizara para la generacion del link de la empresa
        cifrado = hashlib.sha512(nit_empresa.encode("utf-8")).hexdigest()

        #se escribe la url del servidor mas la ruta de la empresa cifrada
        link = f"http://192.168.1.55:5080/menu/{cifrado}"
        return link
    
    def generarQr(self,link):
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=1
        )
        qr.add_data(link)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black",back_color="white")
        nombre_qr = mi_empresa.guardarQr(img)

        return nombre_qr

        
    def guardarQr(self,img):
        fecha_creacion = datetime.now()

        #se convierte en string para añadirlo al nombre del logo
        fecha = fecha_creacion.strftime("%Y%m%d%H%M%S")

        #se crea un nuevo nombre con la letra U y la fecha extraida
        nuevo_qr = f"QR{fecha}.png"
        
        #se guarda la imagen en la carpeta uploads con el nuevo nombre
        img.save("uploads/"+nuevo_qr)

        #se retorna el nuevo nombre de la imagen
        return nuevo_qr

    #metodo para guardar el logo de la empresa en la carpeta uploads
    def guardarFoto(self, logo_empresa):
        #se obtiene la fecha actual
        fecha_creacion = datetime.now()

        #se convierte en string para añadirlo al nombre del logo
        fecha = fecha_creacion.strftime("%Y%m%d%H%M%S")

        #se extrae el nombre del archivo de la extension
        nombre,extension = os.path.splitext(logo_empresa.filename)

        #se crea un nuevo nombre con la letra U y la fecha extraida
        nueva_foto = "U"+fecha+extension
        
        #se guarda la imagen en la carpeta uploads con el nuevo nombre
        logo_empresa.save("uploads/"+nueva_foto)

        #se retorna el nuevo nombre de la imagen
        return nueva_foto
    
    def buscarEmpresaPorNumeroIdentidad(self,numero_identidad):

        #se ejecuta la sentencia sql para buscar el nit de la empresa por medio del numero de identidad
        sql = f"SELECT nit_empresa FROM empresas WHERE numero_identidad = '{numero_identidad}' AND estado = 1"

        mi_cursor = base_datos.cursor()
        mi_cursor.execute(sql)

        #se recogen los datos
        resultado = mi_cursor.fetchall()
        mi_cursor.close()
        print(resultado)

        #se verifica si la empresa tiene asignado un usuario
        if len(resultado) != 0:
            nit_empresa = resultado[0][0]
            #se retorna el nit de la empresa
            return nit_empresa
        else:
            return "no tiene empresa"
    
    #metodo para buscar la empresa por nit
    def buscarEmpresaPorNit(self,nit):
        sql = f"SELECT * FROM empresas WHERE nit_empresa = '{nit}'"

        mi_cursor = base_datos.cursor()
        mi_cursor.execute(sql)

        resultado = mi_cursor.fetchall()
        mi_cursor.close()

        return resultado

    def editarEmpresa(self, nit_empresa,numero_identidad,nombre_empresa,correo_empresa,pais,ciudad,direccion,telefono,logo):

        sql = f"SELECT nit_empresa FROM empresas WHERE numero_identidad = '{numero_identidad}'"
        mi_cursor = base_datos.cursor()
        mi_cursor.execute(sql)
        nit = mi_cursor.fetchall()
        mi_cursor.close()

        #condicional que valida que el nit no haya sido modificado comparando con el nit asignado al numero de identidad del usuario logueado
        if nit_empresa != nit[0][0]:
            return "nit cambiado"
        else:

            #variable donde se guarda la fecha y hora actual en la que se modifica la empresa
            fecha_creacion = datetime.now()

            #verifica si el logo cambia
            if logo != "ninguno":
                logo = mi_empresa.editarLogo(nit_empresa,logo)

                #verifica si el pais cambió
                if pais == "actual":
                    
                    sql = f"UPDATE empresas SET nombre='{nombre_empresa}',correo='{correo_empresa}',ciudad = '{ciudad}', direccion = '{direccion}', telefono='{telefono}',logo='{logo}',fecha_creacion='{fecha_creacion}' WHERE nit_empresa = '{nit_empresa}'"
                else:
                    sql = f"UPDATE empresas SET nombre='{nombre_empresa}',correo='{correo_empresa}',ciudad = '{ciudad}', direccion = '{direccion}', telefono='{telefono}',logo='{logo}',pais='{pais}',fecha_creacion='{fecha_creacion}' WHERE nit_empresa = '{nit_empresa}'"
            else:
                if pais == "actual":
                    sql = f"UPDATE empresas SET nombre='{nombre_empresa}',correo='{correo_empresa}',ciudad = '{ciudad}', direccion = '{direccion}', telefono='{telefono}',fecha_creacion='{fecha_creacion}' WHERE nit_empresa = '{nit_empresa}'"
                else:
                    sql = f"UPDATE empresas SET nombre='{nombre_empresa}',correo='{correo_empresa}',ciudad = '{ciudad}', direccion = '{direccion}', telefono='{telefono}',pais='{pais}',fecha_creacion='{fecha_creacion}' WHERE nit_empresa = '{nit_empresa}'"

            mi_cursor = base_datos.cursor()
            mi_cursor.execute(sql)

            base_datos.commit()
            mi_cursor.close()
            return "empresa creada"

    #metodo para editar la imagen
    def editarLogo(self,id,imagen):

        #metodo para buscar la empresa por nit
        resultado = mi_empresa.buscarEmpresaPorNit(id)

        #recolecta el nombre de la imagen
        nombre_imagen_vieja = resultado[0][9]

        #si habia imagen antes se borra la imagen vieja
        if nombre_imagen_vieja != "no":
            os.remove(os.path.join(web_app.config['CARPETAU'],nombre_imagen_vieja))

        #se recolecta la fecha actual 
        fecha_creacion = datetime.now()

        #la fecha se vuelve string
        fecha = fecha_creacion.strftime("%Y%m%d%H%M%S")

        #se separa el nombre de la extension de la imagen
        nombre,extension = os.path.splitext(imagen.filename)

        #se crea el nuevo nombre con la fecha
        nueva_foto = "P"+fecha+extension
        
        #se guarda la nueva imagen en la carpeta uploads con su nuevo nombre
        imagen.save("uploads/"+nueva_foto)
        
        #se retorna el nuevo nombre de la imagen
        return nueva_foto

    

mi_empresa = Empresas()

