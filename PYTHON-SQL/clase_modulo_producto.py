import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from clase_producto import Producto

class ModuloProducto:
    def __init__(self, root):
        self.producto = Producto()
        self.root = root
        self.root.title("Gestión de Productos")
        self.root.geometry("650x450")
        self.root.resizable(False, False)

        estilo = ttk.Style()
        estilo.theme_use("clam")
        estilo.configure("TLabel", padding=5)
        estilo.configure("TButton", padding=5)
        estilo.configure("TEntry", padding=5)

        # Frame del formulario
        frame_formulario = ttk.LabelFrame(root, text="Datos del Producto", padding=(10, 10))
        frame_formulario.pack(padx=10, pady=10, fill="x")

        ttk.Label(frame_formulario, text="Nombre:").grid(row=0, column=0, sticky="w")
        ttk.Label(frame_formulario, text="Precio:").grid(row=1, column=0, sticky="w")
        ttk.Label(frame_formulario, text="Stock:").grid(row=2, column=0, sticky="w")
        ttk.Label(frame_formulario, text="Categoría:").grid(row=3, column=0, sticky="w")

        self.nombre = ttk.Entry(frame_formulario, width=40)
        self.precio = ttk.Entry(frame_formulario, width=40)
        self.stock = ttk.Entry(frame_formulario, width=40)
        self.categoria = ttk.Entry(frame_formulario, width=40)

        self.nombre.grid(row=0, column=1, padx=5, pady=5)
        self.precio.grid(row=1, column=1, padx=5, pady=5)
        self.stock.grid(row=2, column=1, padx=5, pady=5)
        self.categoria.grid(row=3, column=1, padx=5, pady=5)

        # Frame de botones
        frame_botones = ttk.Frame(root)
        frame_botones.pack(pady=5)

        ttk.Button(frame_botones, text="Agregar", command=self.agregar).grid(row=0, column=0, padx=5)
        ttk.Button(frame_botones, text="Actualizar", command=self.actualizar).grid(row=0, column=1, padx=5)
        ttk.Button(frame_botones, text="Eliminar", command=self.eliminar).grid(row=0, column=2, padx=5)
        ttk.Button(frame_botones, text="Cargar", command=self.cargar_productos).grid(row=0, column=3, padx=5)

        # Tabla
        self.tree = ttk.Treeview(root, columns=("ID", "Nombre", "Precio", "Stock", "Categoria"), show='headings')
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")
        self.tree.pack(padx=10, pady=10, fill="both", expand=True)
        self.tree.bind("<<TreeviewSelect>>", self.seleccionar_fila)

        self.cargar_productos()

    def agregar(self):
        try:
            self.producto.agregar(
                self.nombre.get(),
                float(self.precio.get()),
                int(self.stock.get()),
                self.categoria.get()
            )
            self.cargar_productos()
            self.limpiar_campos()
        except:
            messagebox.showerror("Error", "Datos inválidos")

    def actualizar(self):
        selected = self.tree.selection()
        if not selected:
            return
        item = self.tree.item(selected)
        id_producto = item["values"][0]
        self.producto.actualizar(
            id_producto,
            self.nombre.get(),
            float(self.precio.get()),
            int(self.stock.get()),
            self.categoria.get()
        )
        self.cargar_productos()
        self.limpiar_campos()

    def eliminar(self):
        selected = self.tree.selection()
        if not selected:
            return
        id_producto = self.tree.item(selected)["values"][0]
        self.producto.eliminar(id_producto)
        self.cargar_productos()
        self.limpiar_campos()

    def cargar_productos(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for prod in self.producto.listar():
            self.tree.insert("", "end", values=prod)

    def seleccionar_fila(self, event):
        selected = self.tree.selection()
        if selected:
            item = self.tree.item(selected)
            _, nombre, precio, stock, categoria = item["values"]
            self.nombre.delete(0, tk.END)
            self.precio.delete(0, tk.END)
            self.stock.delete(0, tk.END)
            self.categoria.delete(0, tk.END)
            self.nombre.insert(0, nombre)
            self.precio.insert(0, precio)
            self.stock.insert(0, stock)
            self.categoria.insert(0, categoria)

    def limpiar_campos(self):
        self.nombre.delete(0, tk.END)
        self.precio.delete(0, tk.END)
        self.stock.delete(0, tk.END)
        self.categoria.delete(0, tk.END)

# Para ejecutar la interfaz
if __name__ == "__main__":
    root = tk.Tk()
    app = ModuloProducto(root)
    root.mainloop()
