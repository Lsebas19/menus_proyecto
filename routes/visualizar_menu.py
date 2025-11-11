from conexion import *
from models.visualizar_menu import *


@web_app.route("/menu/<id>")
def menu(id):
    menu = visualizar_mi_menu.buscarMenu(id)

    if menu == "no":
        return render_template("error.html")
    else:
        categorias = visualizar_mi_menu.buscarCategorias(menu[0][0])

        productos = visualizar_mi_menu.buscarProductosMenu(menu[0][0])

        return render_template("visualizar_menu.html",menu = menu,categorias = categorias, productos = productos)
    

@web_app.route("/ordenarCategoriasMenu",methods= ['POST'])
def ordenarCategoriasMenu():
    orden = request.get_json()
    print(orden["menus"])
    visualizar_mi_menu.ordenar_categorias(orden["orden"], orden["menus"])
    



