from conexion import *
import hashlib


class VisualizarMenu:

    def buscarMenu(self,empresa):
        
        sql = f"SELECT menus.id_menu,menus.nombre FROM empresas INNER JOIN menus ON empresas.nit_empresa = menus.nit_empresa WHERE menus.seleccionado = 1 AND empresas.cifrado = '{empresa}' and menus.estado = 1"

        mi_cursor = base_datos.cursor()
        mi_cursor.execute(sql)

        resultado = mi_cursor.fetchall()
        if len(resultado) != 0:
            return resultado
        else:
            return "no"
    
    def buscarCategorias(self,id_menu):
        sql = f"SELECT  c.id_categoria, c.nombre AS nombre_categoria, c.estado, c.fecha_creacion FROM seleccionados s INNER JOIN categorias c ON s.id_categoria = c.id_categoria WHERE s.menu = '{id_menu}' ORDER BY s.posicion ASC;"

        mi_cursor = base_datos.cursor()
        mi_cursor.execute(sql)

        resultado = mi_cursor.fetchall()
        return resultado

    def buscarProductosMenu(self,id_menu):
        sql = f"SELECT  c.id_categoria, c.nombre AS nombre_categoria, p.id_productos, p.nombre AS nombre_producto, p.descripcion, p.presentacion, p.precio, p.imagen FROM seleccionados s INNER JOIN categorias c ON s.id_categoria = c.id_categoria INNER JOIN productos_categorias pc ON c.id_categoria = pc.categorias INNER JOIN productos p ON pc.productos = p.id_productos WHERE s.menu = '{id_menu}' AND p.visible = 1 AND p.estado = 1 ORDER BY c.nombre, p.precio DESC;"

        mi_cursor = base_datos.cursor()
        mi_cursor.execute(sql)

        resultado = mi_cursor.fetchall()
        return resultado

    def ordenar_categorias(self,orden,menu):
        contador = 0

        mi_cursor = base_datos.cursor()

        for id in orden:
            contador = contador + 1
            sql = f"UPDATE seleccionados SET posicion = {contador} WHERE menu = '{menu}' AND id_categoria = '{id}' "

            mi_cursor.execute(sql)
            
        base_datos.commit()
        
        mi_cursor.close()

    
visualizar_mi_menu = VisualizarMenu()