import mysql.connector


class Connection:
    def __init__(self, user, password, database, host):
        self.user = user
        self. password = password
        self. database = database
        self. host = host
        self.conn = None

    def GetConnect():
        if (self.conn == None):
            self. conn == mysql.connector.connect()