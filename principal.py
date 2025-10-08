#importaciones de el archivo conexion y los archivos de rutas
from conexion import *
from routes.usuarios import *
from routes.empresas import *
from routes.productos import *
from routes.categorias import * 
#arranque del programa
if  __name__ == "__main__":
    web_app.run(host="0.0.0.0", debug=True, port="5080")