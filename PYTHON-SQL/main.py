import tkinter as tk
from tkinter import ttk
from clase_modulo_producto import ModuloProducto
from clase_modulo_cliente import ModuloCliente

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión - Tienda")
        self.root.geometry("400x250")
        self.root.resizable(False, False)

        estilo = ttk.Style()
        estilo.theme_use("clam")
        estilo.configure("TButton", font=("Arial", 12), padding=10)
        estilo.configure("TLabel", font=("Arial", 16, "bold"), padding=10)

        frame = ttk.Frame(root, padding=20)
        frame.pack(expand=True)

        ttk.Label(frame, text="Sistema de Gestión").pack(pady=10)

        ttk.Button(frame, text="Módulo de Productos", width=25, command=self.abrir_productos).pack(pady=10)
        ttk.Button(frame, text="Módulo de Clientes", width=25, command=self.abrir_clientes).pack(pady=5)

        # Espacio para agregar más funcionalidades
        # ttk.Button(frame, text="Reportes", width=25, command=self.abrir_reportes).pack(pady=5)

    def abrir_productos(self):
        ventana = tk.Toplevel(self.root)
        ModuloProducto(ventana)

    def abrir_clientes(self):
        ventana = tk.Toplevel(self.root)
        ModuloCliente(ventana)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
