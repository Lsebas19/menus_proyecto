from conexion import *
from models.empresas import *
import random

class Categoria :
    #metodo para sanitizar los campos recibidos de categorias
    def sanitizacionCamposCategorias(self, nombre_categoria):
        #se sanitiza el nombre de la categoria
        nombre_categoriaS = re.sub(r'[^a-zA-Z\ ]', '', nombre_categoria)
        
        #se valida si el nombre de la ategoria cumple con lo esperado
        if len(nombre_categoria) > 4 and len(nombre_categoria) < 59 and nombre_categoriaS == nombre_categoria:
            return "campos correctos"
        else:
            return "nombre de categoria invalido"
        
    #metodo para sanitizar el id de la categoria recibida
    def sanitizarIdCategoria(self,id):
        #se sanitiza el id de la categoria por si se llega a modificar
        id_categoriaS = re.sub(r'[^0-9]', '', id)
        
        #se verifica que el id de la categoria cumpla con lo esperado a recibir
        if len(id_categoriaS) > 0 and len(id_categoriaS) < 5 and id_categoriaS == id:
            return "campos correctos"
        else:
            return "categoria invalida"
        
    #metodo para buscar todas las categorias
    def buscarCategorias(self):
        #se verifica el nit de la empresa asignado al numero de identidad de la persona que inició sesion
        numero_identidad = session.get("numero_identidad")
        resultado =mi_empresa.buscarEmpresaPorNumeroIdentidad(numero_identidad)

        #si el usuario no tiene empresa para buscar las cateogorias
        if resultado == "no tiene empresa":
            return "no tiene empresa"
        
        #se buscan todas las categorias que concuerden con el nit de la empresa y no esten borradas
        sql = f"SELECT * FROM categorias WHERE estado = 1 AND nit_empresa = '{resultado}'"
        mi_cursor = base_datos.cursor()
        mi_cursor.execute(sql)
        categorias = mi_cursor.fetchall()
        mi_cursor.close()
        #retorna las categorias encontradas
        return categorias
    
    #metodo para crear la categoria
    def crearCategoria(self,nombre_categoria):
        #se verifica el nit de la empresa asignado al numero de identidad de la persona que inició sesion
        numero_identidad = session.get("numero_identidad")
        resultado =mi_empresa.buscarEmpresaPorNumeroIdentidad(numero_identidad)

        #si el usuario no itene empresa no avanza
        if resultado == "no tiene empresa":
            return "no tiene empresa"
        
        #se verifica si el nombre de la categoria ya existe para evitar en lo mayor posible las categorias duplicadas
        sql = f"SELECT nombre FROM categorias WHERE '{nombre_categoria}' = nombre AND estado = 1 AND nit_empresa = '{resultado}'"
        mi_cursor = base_datos.cursor()
        mi_cursor.execute(sql)

        #recoleccion de los datos
        resultado = mi_cursor.fetchall()
        mi_cursor.close()
        #condicional que verifica si el nombre de la categoria existe
        if len(resultado) == 1:
            return "categoria ya existe"
        else:
            #metodo para generar el identificador unico de la categoria
            id_categoria = mi_categoria.generarId()

            #metodo para buscar el nit de la empresa
            nit_empresa = mi_empresa.buscarEmpresaPorNumeroIdentidad(numero_identidad)

            #si el usuario no itene empresa no avanza
            if resultado == "no tiene empresa":
                return "no tiene empresa"
            #recolectar la fecha en la que se crea la categoria
            fecha_creacion = datetime.now()

            #insertar los datos de la categoria en la base de datos 
            sql = f"INSERT INTO categorias (id_categoria,nit_empresa,nombre,fecha_creacion) VALUES('{id_categoria}','{nit_empresa}','{nombre_categoria}','{fecha_creacion}')"

            mi_cursor = base_datos.cursor()
            mi_cursor.execute(sql)

            base_datos.commit()
            mi_cursor.close()
            #retorna mensaje de exito
            return "categoria creada"
    
    #metodo para generar el id de la categoria
    def generarId(self):
        
        #ordena las categorias por id de forma descendente para sacar el ultimo id creado
        ciclo = "si"

        while ciclo == "si":
            id = random.randint(0,9999)
             
            sql = f"SELECT id_categoria FROM categorias WHERE id_categoria = '{id}'"
            mi_cursor = base_datos.cursor()
            mi_cursor.execute(sql)

            resultado = mi_cursor.fetchall()
            mi_cursor.close()
            if len(resultado) == 0:
                ciclo = "no"

        return id
    
   
    def buscarCategoriaPorID(self, id):
         #busca la categoria por medio del id
        sql = f"SELECT * FROM categorias WHERE id_categoria = '{id}'"
        mi_cursor = base_datos.cursor()
        mi_cursor.execute(sql)

        resultado = mi_cursor.fetchall()
        mi_cursor.close()
        return resultado

    #metodo para editar la categoria 
    def editarCategoria(self,id,nombre_categoria):
        #verifica el nit de la empresa asignado a el usuario logueado
        numero_identidad = session.get("numero_identidad")
        resultado =mi_empresa.buscarEmpresaPorNumeroIdentidad(numero_identidad)

        #si el usuario no itene empresa no avanza
        if resultado == "no tiene empresa":
            return "no tiene empresa"
        
        #busca si la cateogoria que quiere editar el usuario ya existe
        sql = f"SELECT nombre FROM categorias WHERE '{nombre_categoria}' = nombre AND estado = 1 AND nit_empresa = '{resultado}'"
        mi_cursor = base_datos.cursor()
        mi_cursor.execute(sql)
        
        resultado = mi_cursor.fetchall()
        mi_cursor.close()
        #verifica si el usuario existe
        if len(resultado) == 1:
            return "categoria ya existe"
        else:
            #genera la fecha actual en la que se modifica la categoria
            fecha_creacion = datetime.now()

            sql = f"UPDATE categorias SET nombre = '{nombre_categoria}', fecha_creacion = '{fecha_creacion}' WHERE id_categoria = '{id}'"
            mi_cursor = base_datos.cursor()
            mi_cursor.execute(sql)
            
            base_datos.commit()
            mi_cursor.close()
            return "categoria editada"

    def eliminarCategoria(self, id):

        numero_identidad = session.get("numero_identidad")
        empresa = mi_empresa.buscarEmpresaPorNumeroIdentidad(numero_identidad)

        if empresa == "no tiene empresa":
            return "no tiene empresa"
        else:
            sql = f"SELECT id_categoria FROM categorias WHERE id_categoria = '{id}' AND nit_empresa = '{empresa}' AND estado = 1"

            mi_cursor = base_datos.cursor()
            mi_cursor.execute(sql)

            resultado = mi_cursor.fetchall()
            mi_cursor.close()
            if len(resultado) == 0:
                return "no"
            else:
                
                sql = f"DELETE FROM productos_categorias WHERE categorias = {id} "
                mi_cursor = base_datos.cursor()
                mi_cursor.execute(sql)

                base_datos.commit()
                mi_cursor.close()

                sql = f"DELETE FROM seleccionados WHERE id_categoria = {id} "
                mi_cursor = base_datos.cursor()
                mi_cursor.execute(sql)

                base_datos.commit()
                mi_cursor.close()

                #se cambia el estado de la categoria a 0
                sql = f"UPDATE categorias SET estado = 0 WHERE id_categoria = '{id}'"

                mi_cursor = base_datos.cursor()
                mi_cursor.execute(sql)

                base_datos.commit()
                mi_cursor.close()
                #mensaje de exito de la eliminacion de la categoria
                return "categoria eliminado"


mi_categoria = Categoria()