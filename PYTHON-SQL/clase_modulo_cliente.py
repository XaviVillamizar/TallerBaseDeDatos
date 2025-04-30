import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from clase_cliente import Cliente

class ModuloCliente:
    def __init__(self, root):
        self.cliente = Cliente()
        self.root = root
        self.root.title("Gestión de Clientes")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        # Estilo
        estilo = ttk.Style()
        estilo.theme_use("clam")
        estilo.configure("TLabel", padding=5)
        estilo.configure("TButton", padding=5)
        estilo.configure("TEntry", padding=5)

        # Frame del formulario
        frame_formulario = ttk.LabelFrame(root, text="Datos del Cliente", padding=(10, 10))
        frame_formulario.pack(padx=10, pady=10, fill="x")

        ttk.Label(frame_formulario, text="Nombre:").grid(row=0, column=0, sticky="w")
        ttk.Label(frame_formulario, text="Apellidos:").grid(row=1, column=0, sticky="w")
        ttk.Label(frame_formulario, text="Email:").grid(row=2, column=0, sticky="w")

        self.nombre = ttk.Entry(frame_formulario, width=40)
        self.apellidos = ttk.Entry(frame_formulario, width=40)
        self.email = ttk.Entry(frame_formulario, width=40)

        self.nombre.grid(row=0, column=1, padx=5, pady=5)
        self.apellidos.grid(row=1, column=1, padx=5, pady=5)
        self.email.grid(row=2, column=1, padx=5, pady=5)

        # Frame de botones
        frame_botones = ttk.Frame(root)
        frame_botones.pack(pady=5)

        ttk.Button(frame_botones, text="Agregar", command=self.agregar).grid(row=0, column=0, padx=5)
        ttk.Button(frame_botones, text="Actualizar", command=self.actualizar).grid(row=0, column=1, padx=5)
        ttk.Button(frame_botones, text="Eliminar", command=self.eliminar).grid(row=0, column=2, padx=5)
        ttk.Button(frame_botones, text="Cargar", command=self.cargar_clientes).grid(row=0, column=3, padx=5)

        # Tabla
        self.tree = ttk.Treeview(root, columns=("ID", "Nombre", "Apellidos", "Email"), show='headings')
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")
        self.tree.pack(padx=10, pady=10, fill="both", expand=True)
        self.tree.bind("<<TreeviewSelect>>", self.seleccionar_fila)

        self.cargar_clientes()

    def agregar(self):
        try:
            self.cliente.agregar(
                self.nombre.get(),
                self.apellidos.get(),
                self.email.get()
            )
            self.cargar_clientes()
            self.limpiar_campos()
        except:
            messagebox.showerror("Error", "Datos inválidos")

    def actualizar(self):
        selected = self.tree.selection()
        if not selected:
            return
        id_cliente = self.tree.item(selected)["values"][0]
        self.cliente.actualizar(
            id_cliente,
            self.nombre.get(),
            self.apellidos.get(),
            self.email.get()
        )
        self.cargar_clientes()
        self.limpiar_campos()

    def eliminar(self):
        selected = self.tree.selection()
        if not selected:
            return
        id_cliente = self.tree.item(selected)["values"][0]
        self.cliente.eliminar(id_cliente)
        self.cargar_clientes()
        self.limpiar_campos()

    def cargar_clientes(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for cli in self.cliente.listar():
            self.tree.insert("", "end", values=cli)

    def seleccionar_fila(self, event):
        selected = self.tree.selection()
        if selected:
            item = self.tree.item(selected)
            _, nombre, apellidos, email = item["values"]
            self.nombre.delete(0, tk.END)
            self.apellidos.delete(0, tk.END)
            self.email.delete(0, tk.END)
            self.nombre.insert(0, nombre)
            self.apellidos.insert(0, apellidos)
            self.email.insert(0, email)

    def limpiar_campos(self):
        self.nombre.delete(0, tk.END)
        self.apellidos.delete(0, tk.END)
        self.email.delete(0, tk.END)

# Para ejecutar la interfaz
if __name__ == "__main__":
    root = tk.Tk()
    app = ModuloCliente(root)
    root.mainloop()
