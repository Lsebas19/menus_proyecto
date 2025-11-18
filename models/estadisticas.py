from conexion import *

class Estadisticas:
    def contarProductosPorCategoriasTotales(self, nit_empresa):
        sql = f"SELECT c.nombre AS nombre_categoria, COUNT(pc.productos) AS cantidad_productos FROM categorias c LEFT JOIN productos_categorias pc ON c.id_categoria = pc.categorias LEFT JOIN productos p ON pc.productos = p.id_productos WHERE c.nit_empresa = '{nit_empresa}' GROUP BY c.id_categoria, c.nombre ORDER BY c.nombre;"

        mi_cursor = base_datos.cursor()
        mi_cursor.execute(sql)

        resultado = mi_cursor.fetchall()
        mi_cursor.close()
        return resultado

    def contarProductosPromocionados(self, nit):
        sql = f"SELECT COUNT(id_productos) FROM productos WHERE nit_empresa = '{nit}' AND promocion != 0"

        mi_cursor = base_datos.cursor()
        mi_cursor.execute(sql)

        resultado = mi_cursor.fetchall()
        mi_cursor.close()
        return resultado[0][0]
    
    def contarVisualizacionesMenu(self,nit_empresa):
        sql = f"SELECT COUNT(id) FROM vistas WHERE nit_empresa = '{nit_empresa}' AND MONTH(fecha) = MONTH(CURDATE()) AND YEAR(fecha) = YEAR(CURDATE()) AND DAY(fecha) = DAY(CURDATE())"

        mi_cursor = base_datos.cursor()
        mi_cursor.execute(sql)

        resultado = mi_cursor.fetchall()
        mi_cursor.close()
        return resultado[0][0]
    
    def contarProductosPorCategoriasMenu(self,id_menu):
        sql = f"SELECT  c.nombre AS nombre_categoria, COUNT(pc.productos) AS cantidad_productos FROM seleccionados s INNER JOIN categorias c ON s.id_categoria = c.id_categoria LEFT JOIN productos_categorias pc ON c.id_categoria = pc.categorias LEFT JOIN productos p ON pc.productos = p.id_productos WHERE s.menu = '{id_menu}' GROUP BY c.id_categoria, c.nombre ORDER BY c.nombre;"

        mi_cursor = base_datos.cursor()
        mi_cursor.execute(sql)
        
        resultado = mi_cursor.fetchall()
        mi_cursor.close()
        return resultado

mis_estadisticas = Estadisticas()