from conexion import *
from models.menus import *
from models.empresas import *
from models.productos import *
from models.categorias import *
from models.estadisticas import *

@web_app.route("/estadisticas")
def estadisticas():
    if session.get("login") != True:
        return redirect("/")
    else:
        numero_identidad = session.get("numero_identidad")
        empresa = mi_empresa.buscarEmpresaPorNumeroIdentidad(numero_identidad)
    
        if empresa == "no tiene empresa":
            return redirect("/crearEmpresa")
        else:
            conteo_productos = mi_producto.buscarProductos()
            conteo_productos = len(conteo_productos)

            menu = mi_menu.menuAsignado(empresa)
            conteo_promocionados = mis_estadisticas.contarProductosPromocionados(empresa)
            conteo_productos_categorias_total = mis_estadisticas.contarProductosPorCategoriasTotales(empresa)
            conteo_visualizaciones = mis_estadisticas.contarVisualizacionesMenu(empresa)
            
            if menu == "nada":
                return render_template("estadisticas.html", conteo_productos = conteo_productos, menu = menu, conteo_productos_categorias_total = conteo_productos_categorias_total, visualizaciones = conteo_visualizaciones, promocionados = conteo_promocionados)
            else:
                categorias_menu = mi_menu.buscarCategoriasMenu(menu)
                conteo_productos_categorias_menu = mis_estadisticas.contarProductosPorCategoriasMenu(menu)
                print(conteo_promocionados)
                return render_template("estadisticas.html", conteo_productos = conteo_productos, menu = menu,categorias_menu = categorias_menu, conteo_productos_categorias_total = conteo_productos_categorias_total,conteo_productos_categorias_menu = conteo_productos_categorias_menu, visualizaciones = conteo_visualizaciones, promocionados = conteo_promocionados)