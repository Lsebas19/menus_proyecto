from conexion import *
from models.empresas import *
import random

class Productos:

    #metodo para sanitizar los campos de producto
    def santiziacionCamposProductos(self, nombre_producto,descripcion_producto,presentacion_producto,precio_producto):

        #sanitiza los campos con respecto a lo recolectado 
        nombre_productoS = re.sub(r'[^a-zA-Z0-9\ ]', '', nombre_producto)

        descripcion_productoS = re.sub(r'[^a-zA-Z0-9\,\ ]', '', descripcion_producto)

        presentacion_productoS = re.sub(r'[^a-zA-Z0-9\,\ ]', '', presentacion_producto)

        precio_productoS = re.sub(r'[^0-9]', '', precio_producto)

        #verifica el nombre del producto       
        if len(nombre_producto) > 2 and len(nombre_producto) < 184 and nombre_producto == nombre_productoS:
            #verifica la descripcion
            if len(descripcion_producto) > 5 and len(descripcion_producto) < 151 and descripcion_producto == descripcion_productoS:
                #verifica la presentacion
                if len(presentacion_producto) > 5 and len(presentacion_producto) < 151 and presentacion_producto == presentacion_productoS:
                    
                    #verifica el precio
                    if len(precio_producto) > 3 and len(precio_producto) < 7 and precio_producto == precio_productoS:
                        return "campos correctos"
                    else:
                        return "precio del producto invalido"
                    
                else:
                    return "presentacion del producto invalida"
                
            else:
                return "descripcion invalida"
        else:
            return "nombre invalido"    
        
    #metodo para la creacion del producto
    def crearProducto(self,categoria,nombre_producto,descripcion_producto,presentacion_producto,imagen_producto,precio_producto):
        #recolectar el nit de la empresa del usuario logueado
        numero_identidad = session.get("numero_identidad")
        resultado = mi_empresa.buscarEmpresaPorNumeroIdentidad(numero_identidad)

        #si el usuario no itene empresa no avanza
        if resultado == "no tiene empresa":
            return "no tiene empresa"
    
        #verifica si el nombre del producto ya existe
        sql = f"SELECT nombre FROM productos WHERE nombre = '{nombre_producto}' AND nit_empresa = '{resultado}'"

        mi_cursor = base_datos.cursor()
        mi_cursor.execute(sql)

        resultado = mi_cursor.fetchall()
        mi_cursor.close()

        #condicional que verifica si el nombre ya existe para evitar duplicados
        if len(resultado) > 0:
            return "producto ya existe"
        else:
            #metodo que genera el nuevo id del producto a crear 
            id_nuevo = mi_producto.generarId()

            ##recolectar el nit de la empresa del usuario logueado
            nit_empresa = mi_empresa.buscarEmpresaPorNumeroIdentidad(numero_identidad)

            #si el usuario no itene empresa no avanza
            if resultado == "no tiene empresa":
                return "no tiene empresa"
            #verifica si el usuario agregó imagen del producto
            if imagen_producto.filename != "":

                #metodo que guarda la imagen del producto y genera nuevo nombre unico para la imagen
                imagen = mi_producto.guardarFotoProducto(imagen_producto)
            else:
                #respuesta en caso tal de que el producto no tenga imagen
                imagen = "no"
            
            #recolecta la fecha de creacion del producto
            fecha_creacion = datetime.now()

            #inserta los datos del producto
            sql = f"INSERT INTO productos(id_productos,nombre,descripcion,presentacion,imagen,precio,fecha_creacion,nit_empresa) VALUES('{id_nuevo}','{nombre_producto}','{descripcion_producto}','{presentacion_producto}','{imagen}','{precio_producto}','{fecha_creacion}',{nit_empresa})"

            mi_cursor = base_datos.cursor()
            mi_cursor.execute(sql)

            base_datos.commit()
            mi_cursor.close()

            categorias = []

            categorias.append(categoria)
            #metodo que enlaza el producto con la categoria elegida
            mi_producto.enlazarProductoYCategoria(id_nuevo,categorias)

            #retornar mensaje de exito de producto creado
            return "producto_creado"
            
        
    def generarId(self):

        ciclo = "si"

        while ciclo == "si":
            id = random.randint(0,9999)
             
            sql = f"SELECT id_productos FROM productos WHERE id_productos = '{id}'"
            mi_cursor = base_datos.cursor()
            mi_cursor.execute(sql)

            resultado = mi_cursor.fetchall()
            mi_cursor.close()

            if len(resultado) == 0:
                ciclo = "no"

        return id

    #metodo que guarda la foto del producto
    def guardarFotoProducto(self, imagen):
        #genera la fecha actual
        fecha_creacion = datetime.now()

        #la fecha actual la vuelve string
        fecha = fecha_creacion.strftime("%Y%m%d%H%M%S")

        #separa el nombre de la foto de la extension
        nombre,extension = os.path.splitext(imagen.filename)

        #genera el nuevo nombre de la imagen con la fecha
        nueva_foto = "P"+fecha+extension
        
        #guarda la imagen en la carpeta uploads con el nuevo nombre asignado
        imagen.save("uploads/"+nueva_foto)

        #retorna el nuevo nombre de la imagen
        return nueva_foto

    #metodo que enlaza el producto con la categoria
    def enlazarProductoYCategoria(self,id_producto,categorias):

        #genera un id para la tabla intermedia de productos_categorias
        id = mi_producto.generarIdProducto_Categoria()

        contador = 1

        #inserta el id del producto y el id de la categoria en la tabla intermedia para hacer el enlaze
        sql = f"INSERT INTO productos_categorias(id_tabla,productos,categorias) "

        for categoria in categorias:
            id = mi_producto.generarIdProducto_Categoria()
            if contador == 1:
                
                insertar = f"VALUES('{id}','{id_producto}','{categoria}')"

            else:
                insertar = f",('{id}','{id_producto}','{categoria}')"

            sql = sql+insertar

            contador = contador+1
        
        mi_cursor = base_datos.cursor()
        mi_cursor.execute(sql)

        base_datos.commit()
        mi_cursor.close()
        

    #metodo para generar el id de la tabla intermedia para enlazar producto con categoria
    def generarIdProducto_Categoria(self):
        ciclo = "si"

        while ciclo == "si":
            id = random.randint(0,9999)
            #recolecta el ultimo id creado 
            sql = f"SELECT id_tabla FROM productos_categorias WHERE id_tabla = '{id}'"
            mi_cursor = base_datos.cursor()
            mi_cursor.execute(sql)

            resultado = mi_cursor.fetchall()
            mi_cursor.close()

            if len(resultado) == 0:
                ciclo = "no"

        return id



    #metodo para buscar los productos con sus categorias
    def buscarProductosConCategoria(self):
        #busca el nit de la emresa del usuario logueado
        numero_identidad = session.get("numero_identidad")
        resultado = mi_empresa.buscarEmpresaPorNumeroIdentidad(numero_identidad)

        #si el usuario no itene empresa no avanza
        if resultado == "no tiene empresa":
            return "no tiene empresa"

        #recolecta los datos del producto y el id de la cateogoria que tiene enlazada
        sql = f"SELECT productos.nombre,productos.imagen,productos.descripcion, productos.presentacion,productos.precio, productos_categorias.categorias,productos,id_productos,productos.visible FROM productos INNER JOIN productos_categorias ON productos.id_productos = productos_categorias.productos WHERE productos.nit_empresa = '{resultado}' AND productos.estado = 1 ORDER BY productos.precio DESC"

        mi_cursor = base_datos.cursor()
        mi_cursor.execute(sql)

        resultado = mi_cursor.fetchall()
        mi_cursor.close()

        return resultado

    #metodo para buscar los productos
    def buscarProductos(self):
        #busca el nit de la empresa del usuario logueado
        numero_identidad = session.get("numero_identidad")
        resultado =mi_empresa.buscarEmpresaPorNumeroIdentidad(numero_identidad)

        #si el usuario no itene empresa no avanza
        if resultado == "no tiene empresa":
            return "no tiene empresa"

        #recolecta los productos relacionados con el nit de la empresa y que no esten borrados
        sql = f"SELECT * FROM productos WHERE nit_empresa = '{resultado}' AND estado = 1 ORDER BY precio DESC"
        
        mi_cursor = base_datos.cursor()
        mi_cursor.execute(sql)

        resultado = mi_cursor.fetchall()
        mi_cursor.close()
        return resultado

    #buscar el producto por id
    def buscarProductoPorID(self, id):
        #busca todos los datos del producto con el id proporcionado 
        sql = f"SELECT * FROM productos WHERE id_productos = '{id}'"
        mi_cursor = base_datos.cursor()
        mi_cursor.execute(sql)
        resultado = mi_cursor.fetchall()
        mi_cursor.close()

        return resultado
    
    #metodo para editar producto
    def editarProducto(self,id,nombre_producto,descripcion_producto,presentacion_producto,imagen_producto,precio_producto):

        #busca el nit de la empresa del usuario logueado
        numero_identidad = session.get("numero_identidad")
        resultado = mi_empresa.buscarEmpresaPorNumeroIdentidad(numero_identidad)

        #si el usuario no itene empresa no avanza
        if resultado == "no tiene empresa":
            return "no tiene empresa"

        #buscar el nombre viejo para saber si coincide con el nuevo para que no interfiera en la edicion del producto
        sql = f"SELECT nombre FROM productos WHERE nit_empresa = '{resultado}' AND id_productos = '{id}' "

        mi_cursor = base_datos.cursor()
        mi_cursor.execute(sql)

        nombre_viejo = mi_cursor.fetchall()
        mi_cursor.close()

        #si el nombre viejo es diferente del nuevo se hace la validacion para saber si usa otro nombre que ya existe 
        if nombre_viejo[0][0] != nombre_producto:
            #busca el nombre del producto que se queria editar para saber si existe
            sql = f"SELECT nombre FROM productos WHERE nombre = '{nombre_producto}' AND nit_empresa = '{resultado}'"

            mi_cursor = base_datos.cursor()
            mi_cursor.execute(sql)

            resultado = mi_cursor.fetchall()
            mi_cursor.close()

            #condicional que verifica si el nombre existe para evitar productos duplicados
            if len(resultado) > 0:
                
                return "producto ya existe"
            
        #recolecta la fecha de edicion del producto

        fecha_creacion = datetime.now()

        #verifica si el usuario manda nueva imagen del producto
        if imagen_producto.filename != "":
            #si el usuario manda imagen se llama el metodo para editar la imagen
            imagen = mi_producto.editarImagen(id,imagen_producto)
            #se actualizan datos con la imagen
            sql = f"UPDATE productos SET nombre = '{nombre_producto}', descripcion='{descripcion_producto}',presentacion='{presentacion_producto}',imagen='{imagen}',precio='{precio_producto}', fecha_creacion = '{fecha_creacion}' WHERE id_productos = '{id}'"

        else:
            #si el usuario no agregó imagen se actualizan los datos menos la imagen
            sql = f"UPDATE productos SET nombre = '{nombre_producto}', descripcion='{descripcion_producto}',presentacion='{presentacion_producto}',precio='{precio_producto}', fecha_creacion = '{fecha_creacion}' WHERE id_productos = '{id}'"
        
        mi_cursor = base_datos.cursor()
        mi_cursor.execute(sql)

        base_datos.commit()
        mi_cursor.close()

        #retorna mensaje de exito de edicion del producto
        return "producto editado"
    

    #metodo para editar la imagen
    def editarImagen(self, id,imagen):

        #metodo para buscar el producto por id
        resultado = mi_producto.buscarProductoPorID(id)

        #recolecta el nombre de la imagen
        nombre_imagen_vieja = resultado[0][4]

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
    

    #metodo para eliminar el producto de forma logica 
    def eliminarProducto(self, id):

        numero_identidad = session.get("numero_identidad")
        empresa = mi_empresa.buscarEmpresaPorNumeroIdentidad(numero_identidad)

        if empresa == "no tiene empresa":
            return "no tiene empresa"
        else:
            sql = f"SELECT id_productos FROM productos WHERE id_productos = '{id}' AND nit_empresa = '{empresa}' AND estado = 1"

            mi_cursor = base_datos.cursor()
            mi_cursor.execute(sql)

            resultado = mi_cursor.fetchall()
            mi_cursor.close()
            if len(resultado) == 0:
                return "no"
            else:
                #se cambia el estado del producto a 0
                sql = f"UPDATE productos SET estado = 0 WHERE id_productos = '{id}'"

                mi_cursor = base_datos.cursor()
                mi_cursor.execute(sql)

                base_datos.commit()
                mi_cursor.close()
                #mensaje de exito de la eliminacion del producto
                return "producto eliminado"
    

    def categoriasProducto(self,id_producto):
        #recolecta las categorias que hay enlazadas al producto seleccionado
        sql = f"SELECT * FROM productos_categorias WHERE productos = '{id_producto}'"

        mi_cursor = base_datos.cursor()
        mi_cursor.execute(sql)

        resultado = mi_cursor.fetchall()
        mi_cursor.close()

        return resultado
    
    def asignarCategorias(self, seleccionadas, id):
        resultado_seleccionados = mi_producto.categoriasProducto(id)

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
            mi_producto.enlazarProductoYCategoria(id,agregar)

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
            mi_producto.borrarCategoriasNoAsignadas(id,eliminar)
        return "asignadas"

        

    def borrarCategoriasNoAsignadas(self,id,seleccionadas):

        #sentencia sql incompleta para concatenar posteriormente dependiendo de cuantas categorias haya
        sql = f"DELETE FROM productos_categorias WHERE productos = '{id}' AND categorias IN("

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


    def sanitizarCategoriasSeleccionadas(self,categorias):
        for categoria in categorias:
            print(categoria)
            id_categoriaS = re.sub(r'[^0-9]', '', categoria)
            
            #se verifica que el id de la categoria cumpla con lo esperado a recibir
            if len(id_categoriaS) > 0 and len(id_categoriaS) < 5 and id_categoriaS == categoria:
                validar = "si"
                
            else:
                return "categoria invalida"
        return "campos correctos"

    def promocionProducto(self, precio_nuevo, id, empresa):
        sql = f"UPDATE productos SET promocion = {precio_nuevo} WHERE id_productos = '{id}' AND nit_empresa = '{empresa}'"

        mi_cursor = base_datos.cursor()

        mi_cursor.execute(sql)

        base_datos.commit()

        mi_cursor.close()

        return "promocionado"

    def eliminarPromocionProducto(self,id_producto,nit_empresa):
        sql = f"UPDATE productos SET promocion = 0 WHERE id_productos = '{id_producto}' AND nit_empresa = '{nit_empresa}' AND estado = '1'"
        
        mi_cursor = base_datos.cursor()

        mi_cursor.execute(sql)

        base_datos.commit()

        mi_cursor.close()
        
        return "eliminado"
    

mi_producto = Productos()