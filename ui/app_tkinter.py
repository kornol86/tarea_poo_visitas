import tkinter as tk
from tkinter import ttk, messagebox
from modelos.visitante import Visitante

class App(tk.Tk):
    def __init__(self, servicio):
        super().__init__()
        self.servicio = servicio
        self.title("Sistema de Visitantes")
        self.geometry("800x550")
        self.config(bg="#f4f6f9")

        self.crear_estilos()
        self.crear_widgets()

    def crear_estilos(self):
        style = ttk.Style()
        style.theme_use("default")

        style.configure("Treeview",
                        background="#ffffff",
                        foreground="#333",
                        rowheight=25,
                        fieldbackground="#ffffff")

        style.configure("Treeview.Heading",
                        font=("Helvetica", 11, "bold"))

    def crear_widgets(self):
        # ===== TITULO =====
        titulo = tk.Label(self,
                          text="Sistema de Registro de Visitantes",
                          font=("Segoe UI", 22, "bold"),
                          bg="#f4f6f9",
                          fg="#1a237e")
        titulo.pack(pady=15)

        # ===== CONTENEDOR PRINCIPAL =====
        container = tk.Frame(self, bg="#f4f6f9")
        container.pack(fill="both", expand=True, padx=20)

     # ===== FORMULARIO =====
        frame_form = tk.LabelFrame(container,
                                   text="Datos del Visitante",
                                   font=("Helvetica", 12, "bold"),
                                   bg="#ffffff",
                                   padx=15, pady=15)
        frame_form.pack(fill="x", pady=10)

        tk.Label(frame_form, text="Cédula:", bg="#ffffff").grid(row=0, column=0, sticky="w", pady=5)
        tk.Label(frame_form, text="Nombre:", bg="#ffffff").grid(row=1, column=0, sticky="w", pady=5)
        tk.Label(frame_form, text="Motivo:", bg="#ffffff").grid(row=2, column=0, sticky="w", pady=5)

        self.entry_cedula = tk.Entry(frame_form, width=30)
        self.entry_nombre = tk.Entry(frame_form, width=30)
        self.entry_motivo = tk.Entry(frame_form, width=30)

        self.entry_cedula.grid(row=0, column=1, padx=10)
        self.entry_nombre.grid(row=1, column=1, padx=10)
        self.entry_motivo.grid(row=2, column=1, padx=10)

    # ===== BOTONES =====
        frame_btn = tk.Frame(container, bg="#f4f6f9")
        frame_btn.pack(pady=10)

        frame_btn.columnconfigure((0,1,2), weight=1)

        tk.Button(frame_btn, text="Registrar",
                  bg="#2e7d32", fg="white",
                  font=("Helvetica", 10, "bold"),
                  width=12,
                  command=self.registrar).grid(row=0, column=0, padx=10)

        tk.Button(frame_btn, text="Eliminar",
                  bg="#c62828", fg="white",
                  font=("Helvetica", 10, "bold"),
                  width=12,
                  command=self.eliminar).grid(row=0, column=1, padx=10)

        tk.Button(frame_btn, text="Limpiar",
                  bg="#1565c0", fg="white",
                  font=("Helvetica", 10, "bold"),
                  width=12,
                  command=self.limpiar).grid(row=0, column=2, padx=10)

    # ===== TABLA =====
        frame_tabla = tk.Frame(container, bg="#f4f6f9")
        frame_tabla.pack(fill="both", expand=True)

        self.tree = ttk.Treeview(frame_tabla,
                                 columns=("Cedula", "Nombre", "Motivo"),
                                 show="headings")

        self.tree.heading("Cedula", text="CÉDULA")
        self.tree.heading("Nombre", text="NOMBRE")
        self.tree.heading("Motivo", text="MOTIVO")

        self.tree.pack(fill="both", expand=True)

    def registrar(self):
        cedula = self.entry_cedula.get()
        nombre = self.entry_nombre.get()
        motivo = self.entry_motivo.get()

        if not cedula or not nombre or not motivo:
            messagebox.showwarning("Error", "Todos los campos son obligatorios")
            return

        visitante = Visitante(cedula, nombre, motivo)
        if self.servicio.registrar(visitante):
            messagebox.showinfo("Éxito", "Visitante registrado")
            self.actualizar_tabla()
            self.limpiar()
        else:
            messagebox.showerror("Error", "La cédula ya existe")

    def actualizar_tabla(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for v in self.servicio.listar():
            self.tree.insert("", tk.END, values=(v.cedula, v.nombre, v.motivo))

    def eliminar(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Error", "Seleccione un registro")
            return
        
        item = seleccionado[0]
        cedula = self.tree.item(item)['values'][0]

        if self.servicio.eliminar(cedula):
            messagebox.showinfo("Éxito", "Eliminado correctamente")
            self.actualizar_tabla()

    def limpiar(self):
        self.entry_cedula.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_motivo.delete(0, tk.END)        