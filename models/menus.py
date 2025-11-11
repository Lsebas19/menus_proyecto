from conexion import *
import random
from models.empresas import *


class Menus:
    #metodo para sanitizar los campos recibidos del menú
    def sanitizacionCamposMenu(self, nombre):
        #se sanitiza el nombre de la categoria
        nombreS = re.sub(r'[^a-zA-Z\ ]', '', nombre)
        
        #se valida si el nombre de la ategoria cumple con lo esperado
        if len(nombre) > 4 and len(nombre) < 59 and nombreS == nombre:
            return "campos correctos"
        else:
            return "nombre de menú invalido"
    
    #metodo para generar el id del menú
    def generarId(self):
        
        ciclo = "si"

        while ciclo == "si":
            id = random.randint(0,9999)
             
            sql = f"SELECT id_menu FROM menus WHERE id_menu = '{id}'"
            mi_cursor = base_datos.cursor()
            mi_cursor.execute(sql)

            resultado = mi_cursor.fetchall()
            mi_cursor.close()
            if len(resultado) == 0:
                ciclo = "no"

        return id

    def crearMenu(self,nombre,nit_empresa):
        
        sql = f"SELECT nombre FROM menus WHERE nombre = '{nombre}' AND nit_empresa = '{nit_empresa}' AND estado = 1 "
        mi_cursor = base_datos.cursor()
        mi_cursor.execute(sql)
        resultado_busqueda = mi_cursor.fetchall()
        mi_cursor.close()

        if len(resultado_busqueda) != 0:
            return "este nombre ya existe en tus menus"
        else:
            id = mi_menu.generarId()
            fecha_creacion = datetime.now()

            sql = f"INSERT INTO menus(id_menu,nombre,nit_empresa,fecha_creacion) VALUES('{id}','{nombre}','{nit_empresa}','{fecha_creacion}') "

            mi_cursor = base_datos.cursor()
            mi_cursor.execute(sql)

            base_datos.commit()
            mi_cursor.close()

            return "menu creado"
        
    def buscarMenus(self, nit_empresa):

        sql = f"SELECT * FROM menus WHERE nit_empresa = '{nit_empresa}' AND estado = 1"
        mi_cursor = base_datos.cursor()
        mi_cursor.execute(sql)
        resultado = mi_cursor.fetchall()

        mi_cursor.close()

        return resultado

    def buscarMenuUnico(self, nit_empresa, id):

        sql = f"SELECT * FROM menus WHERE nit_empresa = '{nit_empresa}' AND id_menu = '{id}' AND estado = 1"
        mi_cursor = base_datos.cursor()
        mi_cursor.execute(sql)
        resultado = mi_cursor.fetchall()

        mi_cursor.close()

        if len(resultado) == 0:
            return "menu no existe"
        else:
            return resultado
    
    def editarMenu(self,nombre,nit, id):
        
        sql = f"SELECT nombre FROM menus WHERE nombre = '{nombre}' and nit_empresa = '{nit}' AND estado = 1"
        mi_cursor = base_datos.cursor()
        mi_cursor.execute(sql)
        resultado_busqueda = mi_cursor.fetchall()
        mi_cursor.close()

        if len(resultado_busqueda) != 0:
            return "este nombre ya existe en tus menus"
        else:
            
            fecha_creacion = datetime.now()
            print(nombre)
            sql = f"UPDATE menus SET nombre='{nombre}',fecha_creacion = '{fecha_creacion}' WHERE id_menu = '{id}' AND nit_empresa = '{nit}' AND estado = 1"

            print(sql)
            mi_cursor = base_datos.cursor()
            mi_cursor.execute(sql)

            base_datos.commit()
            mi_cursor.close()

            return "menu editado"

    def categoriasMenu(self,id_menu):
        #recolecta las categorias que hay enlazadas al producto seleccionado
        sql = f"SELECT * FROM seleccionados WHERE menu = '{id_menu}'"

        mi_cursor = base_datos.cursor()
        mi_cursor.execute(sql)

        resultado = mi_cursor.fetchall()
        mi_cursor.close()

        return resultado

    def asignarCategorias(self, seleccionadas, id):
        resultado_seleccionados = mi_menu.categoriasMenu(id)

        #inicializa una variable donde se van a guardar las categorias que proximamente se van a enlazar con el producto
        agregar = []
        
        #se recorre la lista de las categorias recolectadas en el frontend
        for seleccionado in seleccionadas :

            #se inicializa la variable en no por si la categoria seleccionada no se encuentra en la base de datos enlazada con el producto
            encontrado = "no"
            for elegido in resultado_seleccionados:
                print(elegido[2])
                print(seleccionado)
                #si la categoria ya está enlazada con el producto se cambia el valor de la variable a si
                if elegido[2] == seleccionado:
                    encontrado = "si"
            #las categorias que no se encontraron enlazadas a la base de datos se agregan a la variable para enlazarlas
            if encontrado == "no":
                agregar.append(seleccionado)
                
        #si la lista no viene vacia procede a enlazar las categorias con el producto
        if len(agregar) > 0:
            mi_menu.enlazarMenuYCategoria(id,agregar)

        eliminar = []

        #for que recorre la lista de las categorias enlazadas para comparar con las seleccionadas y asi buscar las categorias que ya no estan seleccionadas para borrarlas
        for elegido in resultado_seleccionados:
            encontrado = "no"

            for seleccionado in seleccionadas:
                #si se encuentra la categoria seleccionada con las que ya estaban no se agrega a la variable para eliminar
                if elegido[2] == seleccionado:
                    encontrado = "si"
            if encontrado == "no":
                eliminar.append(elegido[2])

        #si hay alguna categorias para desenlazar se llama al metodo
        if len(eliminar) > 0:
            mi_menu.borrarCategoriasNoAsignadas(id,eliminar)
        return "asignadas"

    def enlazarMenuYCategoria(self,menu,categorias):

        #genera un id para la tabla intermedia de productos_categorias
        id = mi_menu.generarIdMenu_Categoria()

        contador = 1

        #inserta el id del producto y el id de la categoria en la tabla intermedia para hacer el enlaze
        sql = f"INSERT INTO seleccionados(id_seleccionado,menu,id_categoria) "

        for categoria in categorias:
            id = mi_menu.generarIdMenu_Categoria()
            if contador == 1:
                
                insertar = f"VALUES('{id}','{menu}','{categoria}')"

            else:
                insertar = f",('{id}','{menu}','{categoria}')"

            sql = sql+insertar

            contador = contador+1
        
        mi_cursor = base_datos.cursor()
        mi_cursor.execute(sql)

        base_datos.commit()
        mi_cursor.close()

    #metodo para generar el id de la tabla intermedia para enlazar producto con categoria
    def generarIdMenu_Categoria(self):
        ciclo = "si"

        while ciclo == "si":
            id = random.randint(0,9999)
            #recolecta el ultimo id creado 
            sql = f"SELECT id_seleccionado FROM seleccionados WHERE id_seleccionado = '{id}'"
            mi_cursor = base_datos.cursor()
            mi_cursor.execute(sql)

            resultado = mi_cursor.fetchall()
            mi_cursor.close()

            if len(resultado) == 0:
                ciclo = "no"

        return id

    def borrarCategoriasNoAsignadas(self,id,seleccionadas):

        #sentencia sql incompleta para concatenar posteriormente dependiendo de cuantas categorias haya
        sql = f"DELETE FROM seleccionados WHERE menu = '{id}' AND id_categoria IN("

        contador = 1

        for seleccionado in seleccionadas:
            if contador == 1:
                eliminar = f"'{seleccionado}'"
            else:
                eliminar = f",'{seleccionado}'"
            sql = sql+eliminar
            contador = contador+1
        sql = sql+")"
        print (sql)
        mi_cursor = base_datos.cursor()
        mi_cursor.execute(sql)
        base_datos.commit()
        mi_cursor.close()

    def buscarCategoriasMenu(self, menu):
        sql = f"SELECT * FROM categorias INNER JOIN seleccionados ON seleccionados.id_categoria = categorias.id_categoria WHERE seleccionados.menu = '{menu}' ORDER BY seleccionados.posicion ASC"
        mi_cursor = base_datos.cursor()
        mi_cursor.execute(sql)

        resultado = mi_cursor.fetchall()
        mi_cursor.close()

        return resultado

    def eliminarMenu(self, id_menu):
        numero_identidad = session.get("numero_identidad")
        empresa = mi_empresa.buscarEmpresaPorNumeroIdentidad(numero_identidad)

        if empresa == "no tiene empresa":
            return "no tiene empresa"
        else:
            sql = f"SELECT id_menu FROM menus WHERE id_menu = '{id_menu}' AND nit_empresa = '{empresa}' AND estado = 1"

            mi_cursor = base_datos.cursor()
            mi_cursor.execute(sql)

            resultado_menu = mi_cursor.fetchall()
            mi_cursor.close()
            if len(resultado_menu) == 0:
                return "no"
            else:
                sql = f"UPDATE menus SET estado = 0 WHERE id_menu = '{id_menu}'"
                mi_cursor = base_datos.cursor()
                mi_cursor.execute(sql)
                base_datos.commit()
                mi_cursor.close()
                return "eliminado"
            
    def asignarMenu(self,id_menu, empresa):
        sql = f"SELECT id_menu FROM menus WHERE nit_empresa = {empresa} AND seleccionado = 1"
        mi_cursor = base_datos.cursor()
        mi_cursor.execute(sql)
        resultado = mi_cursor.fetchall()

        if len(resultado) != 0:
            sql = f"UPDATE menus SET seleccionado = 0 WHERE id_menu = '{resultado[0][0]}'"
            mi_cursor = base_datos.cursor()
            mi_cursor.execute(sql)
            base_datos.commit()

        sql = f"UPDATE menus SET  seleccionado = 1 WHERE nit_empresa = '{empresa}' AND id_menu = '{id_menu}'"
        mi_cursor = base_datos.cursor()
        mi_cursor.execute(sql)
        base_datos.commit()

        return "asignado"

    def menuAsignado(self, nit_empresa):
        sql = f"SELECT id_menu FROM menus WHERE nit_empresa = {nit_empresa} AND seleccionado = 1"
        mi_cursor = base_datos.cursor()
        mi_cursor.execute(sql)
        resultado = mi_cursor.fetchall()

        if len(resultado) != 0:
            resultado = resultado[0][0]
            return resultado
        else:
            return "nada" 


mi_menu = Menus()