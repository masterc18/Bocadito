import mysql.connector
import os

conexion = mysql.connector.connect(
    user="root",
    password="carlosftg1923",
    host="localhost",
    database = "Bocadito",
    port = "3306"
)
print(conexion)
