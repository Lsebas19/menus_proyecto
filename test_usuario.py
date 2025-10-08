from conexion import *
from models.usuarios import *
import pytest
import hashlib


class Test_IniciarSesion:
    def setup_class(self):
        # Se prepara el entorno de prueba
        cifrada = hashlib.sha512("19022007".encode("UTF-8")).hexdigest()
        sql = f"INSERT INTO usuarios (numero_identidad,contrasena) VALUES ('1115070113','{cifrada}')"
        mi_cursor.execute(sql)
        base_datos.commit()

    @pytest.mark.parametrize(
        ["numero_identidad","contrasena","esperado"],
        [("1115070113","19022007","encontrado"),
        ("1115070113","1748141","no encontrado"),
        ("1141414123","djlfsk","no encontrado")]
    )
    
    def test_valida_login(self,numero_identidad,contrasena,esperado):
        # Se ejecuta la prueba
        resultado = mi_usuario.comprobarUsuario(numero_identidad,contrasena)
        # Se verifica el resultado
        assert resultado == esperado


    def teardown_class(self):
        # Se limpia la base de datos
        sql=f"DELETE FROM usuarios WHERE numero_identidad='1115070113'"
        mi_cursor.execute(sql)
        base_datos.commit()



class Test_comprobarEmpresaUsuario:
    def setup_class(self):
        # Se prepara el entorno de prueba
        sql = f"INSERT INTO usuarios (numero_identidad) VALUES ('1234567891'),('1987654321')"
        mi_cursor.execute(sql)
        base_datos.commit()

        sql = f"INSERT INTO empresas (nit_empresa,numero_identidad) VALUES('1122334455','1234567891')"
        mi_cursor.execute(sql)
        base_datos.commit()

    @pytest.mark.parametrize(
        ["numero_identidad","esperado"],
        [("1234567891","tiene empresa"),
        ("1987654321","no tiene empresa")]
    )

    def test_comprobarEmpresa(self,numero_identidad,esperado):
        # Se ejecuta la prueba
        resultado = mi_usuario.comprobarEmpresa(numero_identidad)
        # Se verifica el resultado
        assert resultado == esperado
        
    def teardown_class(self):
        # Se limpia la base de datos
        sql1=f"DELETE FROM empresas WHERE nit_empresa='1122334455'"
        mi_cursor.execute(sql1)
        base_datos.commit()

        sql2=f"DELETE FROM usuarios WHERE numero_identidad='1234567891'"
        mi_cursor.execute(sql2)
        base_datos.commit()

        sql3=f"DELETE FROM usuarios WHERE numero_identidad='1987654321'"
        mi_cursor.execute(sql3)
        base_datos.commit()
