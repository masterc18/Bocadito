import mysql.connector
import os
# forma 1 de conectar la base de datos


class Connection:
    def __init__(self, host, database, port, user, password):
        self.host = host
        self.database = database
        self.port = port
        self.user = user
        self.password = password
        self.conn = None

    def getConnect(self):
        if self.conn == None:
            self.conn = mysql.connector.connect(
                host=self.host,
                database=self.database,
                port=self.port,
                user=self.user,
                password=self.password
            )
            return self.conn

    def getDisconnect(self):
        if self.conn != None:
            self.conn.close()
            self.conn = None


x = Connection("Localhost", "Bocadito", "3306", "root", "carlosftg1923")
conn = x.getConnect()

if conn != None:
    print("conexion exitosa")
    print(conn)
else:
    print("Error de conexion")


# Forma 2 de conectar una base de datos
# conexion = mysql.connector.connect(
#     user="root",
#     password="carlosftg1923",
#     host="localhost",
#     database = "Bocadito",
#     port = "3306"
# )
# print(conexion)
