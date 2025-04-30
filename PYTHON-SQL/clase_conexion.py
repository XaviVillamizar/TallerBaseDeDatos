import mysql.connector

class Conexion:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = ""  # pon tu contraseña si la tienes
        self.database = "tienda_db"

    def conectar(self):
        try:
            conexion = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            return conexion
        except mysql.connector.Error as err:
            print(f"Error de conexión: {err}")
            return None
