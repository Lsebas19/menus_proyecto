#importaciones
from datetime import datetime, timedelta
from flask import Flask,request, render_template, redirect, session
import mysql.connector
import os
import re


#conexion con la base de datos
base_datos = mysql.connector.connect(host="localhost",
                                    port="3306",
                                    user="root",
                                    password="",
                                    database="menus_editables")

#creacion del cursor
mi_cursor = base_datos.cursor()

#instancia del programa
web_app = Flask(__name__)

web_app.config['CARPETAU'] = os.path.join('uploads')

web_app.secret_key = "LaMasSegura"

