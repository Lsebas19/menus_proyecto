from conexion import *
import requests
import socket
import random
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
        
        
    def obtenerIpCliente(self):
        respuesta = requests.get('http://checkip.amazonaws.com')
        respuesta.raise_for_status()
        return respuesta.text.strip()

    def agregarVista(self, empresa):
        ip = visualizar_mi_menu.obtenerIpCliente()
        ip_local = visualizar_mi_menu.recolectarIpLocal()
        print(ip)
        print(ip_local)
        sql = f"SELECT id FROM vistas WHERE ip_publica = '{ip}' AND ip_local = '{ip_local}' AND nit_empresa = '{empresa}' AND MONTH(fecha) = MONTH(CURDATE()) AND YEAR(fecha) = YEAR(CURDATE()) AND DAY(fecha) = DAY(CURDATE())"
        
        mi_cursor = base_datos.cursor()
        mi_cursor.execute(sql)
        resultado = mi_cursor.fetchall()
        mi_cursor.close()
        
        if len(resultado) == 0:
            id = visualizar_mi_menu.generarIdVisualizacion()
            fecha = datetime.now()
            sql = f"INSERT INTO vistas VALUES ('{id}','{ip}','{fecha}','{empresa}','{ip_local}')"
            mi_cursor = base_datos.cursor()
            
            mi_cursor.execute(sql)
            base_datos.commit()
            mi_cursor.close()
    
    def recolectarIpLocal(self):
        ip_local = request.headers.get('X-Forwarded-For', request.remote_addr)
        return ip_local
    
    def generarIdVisualizacion(self):
        ciclo = "si"

        while ciclo == "si":
            id = random.randint(0,999999)
            #recolecta el ultimo id creado 
            sql = f"SELECT id FROM vistas WHERE id = '{id}'"
            mi_cursor = base_datos.cursor()
            mi_cursor.execute(sql)

            resultado = mi_cursor.fetchall()
            mi_cursor.close()

            if len(resultado) == 0:
                ciclo = "no"
        return id
        
    def encontrarEmpresa(self, cifrado):
        sql = f"SELECT nit_empresa FROM empresas WHERE cifrado = '{cifrado}'"
        mi_cursor = base_datos.cursor()
        mi_cursor.execute(sql)

        resultado = mi_cursor.fetchall()
        mi_cursor.close()
        return resultado[0][0]
    
visualizar_mi_menu = VisualizarMenu()