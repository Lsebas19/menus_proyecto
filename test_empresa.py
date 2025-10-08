from conexion import *
from models.empresas import *
import pytest


class Test_crearEmpresa:
    def setup_class(self):
        # Se prepara el entorno de prueba
        sql = f"INSERT INTO usuarios (numero_identidad) VALUES ('987654321')"
        mi_cursor.execute(sql)
        base_datos.commit()
        
        sql = f"INSERT INTO empresas (nit_empresa,numero_identidad) VALUES ('123454321','987654321')"
        mi_cursor.execute(sql)
        base_datos.commit()

        

    @pytest.mark.parametrize(
        ["nit_empresa","numero_identidad","nombre_empresa","correo_empresa","pais","ciudad","direccion","telefono","logo","esperado"],

        [("11223344","987654321","coca cola","juansebas@gmail.com","colombia","tulua","123322","3188907917","ninguno","empresa creada"),
         ("123454321","987654321","coca cola","juansebas@gmail.com","colombia","tulua","123322","3188907917","ninguno","empresa ya existe")
        ]
    )
    
    def test_creaEmpresa(self,nit_empresa,numero_identidad,nombre_empresa,correo_empresa,pais,ciudad,direccion,telefono,logo,esperado):
        # Se ejecuta la prueba
        resultado = mi_empresa.agregarEmpresa(nit_empresa,numero_identidad,nombre_empresa,correo_empresa,pais,ciudad,direccion,telefono,logo)
        # Se verifica el resultado
        assert resultado == esperado


    def teardown_class(self):
        # Se limpia la base de datos
        sql=f"DELETE FROM empresas WHERE nit_empresa='123454321'"
        mi_cursor.execute(sql)
        base_datos.commit()

        sql=f"DELETE FROM empresas WHERE nit_empresa='11223344'"
        mi_cursor.execute(sql)
        base_datos.commit()

        sql=f"DELETE FROM usuarios WHERE numero_identidad='987654321'"
        mi_cursor.execute(sql)
        base_datos.commit()

    
class Test_buscarEmpresaPorNumeroIdentidad:
    def setup_class(self):

        sql = f"INSERT INTO usuarios (numero_identidad) VALUES ('987654321'),('1223344598')"
        mi_cursor.execute(sql)
        base_datos.commit()
        
        sql = f"INSERT INTO empresas (nit_empresa,numero_identidad) VALUES ('123454321','987654321')"
        mi_cursor.execute(sql)
        base_datos.commit()

    @pytest.mark.parametrize(
        ["numero_identidad","esperado"],
        [("987654321","lleno"),
         ("1223344598","vacio")]
    )

    def test_buscarEmpresaPorNumeroIdentidad(self,numero_identidad,esperado):

        respuesta = mi_empresa.buscarEmpresaPorNumeroIdentidad(numero_identidad)
        print(respuesta)
        if respuesta != "no tiene empresa":
            resultado = "lleno"
            
        
        else:
            resultado = "vacio"

        assert resultado == esperado

    def teardown_class(self):
        
        sql=f"DELETE FROM empresas WHERE nit_empresa='123454321'"
        mi_cursor.execute(sql)
        base_datos.commit()

        sql=f"DELETE FROM usuarios WHERE numero_identidad='987654321'"
        mi_cursor.execute(sql)
        base_datos.commit()

        sql=f"DELETE FROM usuarios WHERE numero_identidad='1223344598'"
        mi_cursor.execute(sql)
        base_datos.commit()


class Test_editarEmpresa:
    def setup_class(self):
        sql = f"INSERT INTO empresas (nit_empresa,numero_identidad) VALUES ('123454321','987654321')"
        mi_cursor.execute(sql)
        base_datos.commit()
    
    @pytest.mark.parametrize(
        ["nit_empresa","numero_identidad","correo","pais","ciudad","direccion","telefono","logo","esperado"],
        [("987654321","lleno"),
         ("1223344598","vacio")]
    )

    def test_agregarEmpresa(self):
        return "hola"
