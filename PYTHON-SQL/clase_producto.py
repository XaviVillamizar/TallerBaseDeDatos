from clase_conexion import Conexion

class Producto:
    def __init__(self):
        self.con = Conexion()

    def agregar(self, nombre, precio, stock, categoria):
        conn = self.con.conectar()
        cursor = conn.cursor()
        sql = "INSERT INTO productos (nombre, precio, stock, categoria) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (nombre, precio, stock, categoria))
        conn.commit()
        conn.close()

    def listar(self):
        conn = self.con.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        conn.close()
        return productos

    def eliminar(self, id_producto):
        conn = self.con.conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM productos WHERE id = %s", (id_producto,))
        conn.commit()
        conn.close()

    def actualizar(self, id_producto, nombre, precio, stock, categoria):
        conn = self.con.conectar()
        cursor = conn.cursor()
        sql = "UPDATE productos SET nombre=%s, precio=%s, stock=%s, categoria=%s WHERE id=%s"
        cursor.execute(sql, (nombre, precio, stock, categoria, id_producto))
        conn.commit()
        conn.close()
