from clase_conexion import Conexion

class Cliente:
    def __init__(self):
        self.con = Conexion()

    def agregar(self, nombre, apellidos, email):
        conn = self.con.conectar()
        cursor = conn.cursor()
        sql = "INSERT INTO clientes (nombre, apellidos, email) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nombre, apellidos, email))
        conn.commit()
        conn.close()

    def listar(self):
        conn = self.con.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()
        conn.close()
        return clientes

    def eliminar(self, id_cliente):
        conn = self.con.conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM clientes WHERE id = %s", (id_cliente,))
        conn.commit()
        conn.close()

    def actualizar(self, id_cliente, nombre, apellidos, email):
        conn = self.con.conectar()
        cursor = conn.cursor()
        sql = "UPDATE clientes SET nombre=%s, apellidos=%s, email=%s WHERE id=%s"
        cursor.execute(sql, (nombre, apellidos, email, id_cliente))
        conn.commit()
        conn.close()
