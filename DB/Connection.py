import mysql.connector
import os

# Se crea la clase conexion con los atributos
class Connection:
    def __init__(self, user, password, database, host):
        self.user = user
        self.password = password
        self.database = database
        self.host = host
        self.conn = None

    #Se crea el metodo de obtener la conexion con la base de datos
    def GetConnect(self):
        if (self.conn == None):
            self. conn == mysql.connector.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                database=self.database
            )
            return self.conn

    # se crea el metodo para desconectar la base datos
    def GetDisconnect(self):
        if (self.conn != None):
            self.conn.close()
            self.conn = None
