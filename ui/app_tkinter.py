import tkinter as tk
from tkinter import ttk, messagebox
from modelos.visitante import Visitante

class App(tk.Tk):
    def __init__(self, servicio):
        super().__init__()
        self.servicio = servicio
        self.title("Sistema de Visitantes")
        self.geometry("700x500")
        self.config(bg="#e3f2fd")

        self.crear_widgets()

    def crear_widgets(self):
        # Formulario
        frame_form = tk.Frame(self, bg="#e3f2fd")
        frame_form.pack(pady=10)

        tk.Label(frame_form, text="Cédula", bg="#e3f2fd").grid(row=0, column=0)
        tk.Label(frame_form, text="Nombre", bg="#e3f2fd").grid(row=1, column=0)
        tk.Label(frame_form, text="Motivo", bg="#e3f2fd").grid(row=2, column=0)

        self.entry_cedula = tk.Entry(frame_form)
        self.entry_nombre = tk.Entry(frame_form)
        self.entry_motivo = tk.Entry(frame_form)

        self.entry_cedula.grid(row=0, column=1)
        self.entry_nombre.grid(row=1, column=1)
        self.entry_motivo.grid(row=2, column=1)

# Botones
        frame_btn = tk.Frame(self, bg="#e3f2fd")
        frame_btn.pack(pady=10)
        tk.Button(frame_btn, text="Registrar", bg="#4caf50", fg="white", command=self.registrar).grid(row=0, column=0, padx=5)
        tk.Button(frame_btn, text="Eliminar", bg="#f44336", fg="white", command=self.eliminar).grid(row=0, column=1, padx=5)
        tk.Button(frame_btn, text="Limpiar", bg="#2196f3", fg="white", command=self.limpiar).grid(row=0, column=2, padx=5)
    
        # Tabla
        self.tree = ttk.Treeview(self, columns=("Cedula", "Nombre", "Motivo"), show="headings")
        self.tree.heading("Cedula", text="Cédula")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Motivo", text="Motivo")
        self.tree.pack(fill=tk.BOTH, expand=True, pady=10)

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

        cedula = self.tree.item(seleccionado)['values'][0]
        if self.servicio.eliminar(cedula):
            messagebox.showinfo("Éxito", "Eliminado correctamente")
            self.actualizar_tabla()

    def limpiar(self):
        self.entry_cedula.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_motivo.delete(0, tk.END)