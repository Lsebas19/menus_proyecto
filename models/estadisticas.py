from conexion import *

class Estadisticas:
    def contarProductosPorCategoriasTotales(self, nit_empresa):
        sql = f"SELECT c.nombre AS nombre_categoria, COUNT(pc.productos) AS cantidad_productos FROM categorias c LEFT JOIN productos_categorias pc ON c.id_categoria = pc.categorias LEFT JOIN productos p ON pc.productos = p.id_productos WHERE c.nit_empresa = '{nit_empresa}' GROUP BY c.id_categoria, c.nombre ORDER BY c.nombre;"

        mi_cursor = base_datos.cursor()
        mi_cursor.execute(sql)

        resultado = mi_cursor.fetchall()
        mi_cursor.close()
        return resultado

    def contarProductosPorCategoriasMenu(self,id_menu):
        sql = f"SELECT  c.nombre AS nombre_categoria, COUNT(pc.productos) AS cantidad_productos FROM seleccionados s INNER JOIN categorias c ON s.id_categoria = c.id_categoria LEFT JOIN productos_categorias pc ON c.id_categoria = pc.categorias LEFT JOIN productos p ON pc.productos = p.id_productos WHERE s.menu = '{id_menu}' GROUP BY c.id_categoria, c.nombre ORDER BY c.nombre;"

        mi_cursor = base_datos.cursor()
        mi_cursor.execute(sql)
        
        resultado = mi_cursor.fetchall()
        mi_cursor.close()
        return resultado

mis_estadisticas = Estadisticas()