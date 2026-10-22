# home_view.py
import tkinter as tk
from tkinter import messagebox, ttk
from products_model import SistemaModel


class DashboardVentana:

  def __init__(self, root, usuario_activo, rol_activo):
    self.root = root
    self.root.title("Panel Principal - Sistema de Papelería")
    self.root.geometry("860x560")
    self.root.configure(bg="#232326")

    self.model = SistemaModel()
    self._configurar_estilos()

    # Encabezado
    lbl_bienvenida = tk.Label(
        self.root,
        text=f"Bienvenido/a, {usuario_activo} ({rol_activo})",
        font=("Helvetica", 12, "bold"),
        fg="#ffffff",
        bg="#232326",
    )
    lbl_bienvenida.pack(pady=(15, 10))

    # Pestañas
    self.notebook = ttk.Notebook(self.root)
    self.notebook.pack(fill="both", expand=True, padx=20, pady=(0, 20))

    self.tab_inicio = tk.Frame(self.notebook, bg="#1a1a1c")
    self.tab_inventario = tk.Frame(self.notebook, bg="#1a1a1c")

    self.notebook.add(self.tab_inicio, text="Inicio")
    self.notebook.add(self.tab_inventario, text="Inventario de Productos")
    self.notebook.select(self.tab_inventario)

    self._crear_pestana_inicio(usuario_activo, rol_activo)
    self._crear_modulo_inventario()
    self._cargar_productos()

  def _configurar_estilos(self):
    style = ttk.Style()
    style.theme_use("clam")

    style.configure("TNotebook", background="#232326", borderwidth=0)
    style.configure(
        "TNotebook.Tab",
        background="#38383b",
        foreground="#d0d0d0",
        padding=[12, 5],
        font=("Helvetica", 9),
    )
    style.map(
        "TNotebook.Tab",
        background=[("selected", "#505055")],
        foreground=[("selected", "#ffffff")],
    )

    style.configure(
        "Treeview",
        background="#18181a",
        foreground="#ffffff",
        fieldbackground="#18181a",
        rowheight=25,
        font=("Helvetica", 10),
    )
    style.configure(
        "Treeview.Heading",
        background="#28282b",
        foreground="#ffffff",
        font=("Helvetica", 9, "bold"),
    )
    style.map("Treeview", background=[("selected", "#3b3b42")])

  def _crear_pestana_inicio(self, usuario, rol):
    lbl = tk.Label(
        self.tab_inicio,
        text=(
            f"Sesión activa: {usuario}\nRol:"
            f" {rol}\n\nSelecciona la pestaña 'Inventario de Productos' para"
            " gestionar el almacén."
        ),
        font=("Helvetica", 11),
        fg="#cccccc",
        bg="#1a1a1c",
        justify="center",
    )
    lbl.pack(expand=True)

  def _crear_modulo_inventario(self):
    contenedor = tk.Frame(self.tab_inventario, bg="#1a1a1c")
    contenedor.pack(fill="both", expand=True, padx=15, pady=15)

    # Formulario lateral izquierdo
    frame_form = tk.LabelFrame(
        contenedor,
        text=" Registrar Producto ",
        font=("Helvetica", 9, "bold"),
        fg="#ffffff",
        bg="#1a1a1c",
        padx=12,
        pady=12,
        relief="groove",
    )
    frame_form.pack(side="left", fill="y", padx=(0, 15))

    tk.Label(
        frame_form,
        text="Nombre:",
        font=("Helvetica", 9, "bold"),
        fg="#ffffff",
        bg="#1a1a1c",
    ).pack(anchor="w", pady=(2, 2))
    self.entry_nombre = tk.Entry(
        frame_form,
        bg="#111113",
        fg="#ffffff",
        insertbackground="white",
        font=("Helvetica", 10),
    )
    self.entry_nombre.pack(fill="x", ipady=2, pady=(0, 8))

    tk.Label(
        frame_form,
        text="Código:",
        font=("Helvetica", 9, "bold"),
        fg="#ffffff",
        bg="#1a1a1c",
    ).pack(anchor="w", pady=(2, 2))
    self.entry_codigo = tk.Entry(
        frame_form,
        bg="#111113",
        fg="#ffffff",
        insertbackground="white",
        font=("Helvetica", 10),
    )
    self.entry_codigo.pack(fill="x", ipady=2, pady=(0, 8))

    tk.Label(
        frame_form,
        text="Cantidad / Stock:",
        font=("Helvetica", 9, "bold"),
        fg="#ffffff",
        bg="#1a1a1c",
    ).pack(anchor="w", pady=(2, 2))
    self.entry_cantidad = tk.Entry(
        frame_form,
        bg="#111113",
        fg="#ffffff",
        insertbackground="white",
        font=("Helvetica", 10),
    )
    self.entry_cantidad.pack(fill="x", ipady=2, pady=(0, 15))

    btn_guardar = tk.Button(
        frame_form,
        text="Guardar Producto",
        font=("Helvetica", 9, "bold"),
        bg="#ffffff",
        fg="#000000",
        relief="flat",
        cursor="hand2",
        command=self._guardar_producto,
    )
    btn_guardar.pack(fill="x", ipady=4)

    # Tabla a la derecha
    columnas = ("ID", "Nombre", "Código", "Cantidad", "Estado")
    self.tabla = ttk.Treeview(
        contenedor, columns=columnas, show="headings", selectmode="browse"
    )

    self.tabla.heading("ID", text="ID")
    self.tabla.heading("Nombre", text="Nombre")
    self.tabla.heading("Código", text="Código")
    self.tabla.heading("Cantidad", text="Cantidad")
    self.tabla.heading("Estado", text="Estado")

    self.tabla.column("ID", width=50, anchor="center")
    self.tabla.column("Nombre", width=180, anchor="w")
    self.tabla.column("Código", width=100, anchor="center")
    self.tabla.column("Cantidad", width=80, anchor="center")
    self.tabla.column("Estado", width=100, anchor="center")

    self.tabla.pack(side="left", fill="both", expand=True)

  def _cargar_productos(self):
    for item in self.tabla.get_children():
      self.tabla.delete(item)

    productos = self.model.obtener_productos()
    for p in productos:
      fila = (
          p.get("id_product"),
          p.get("name"),
          p.get("code"),
          p.get("quantity"),
          p.get("state"),
      )
      self.tabla.insert("", tk.END, values=fila)

  def _guardar_producto(self):
    nom = self.entry_nombre.get().strip()
    cod = self.entry_codigo.get().strip()
    cant_str = self.entry_cantidad.get().strip()

    if not nom or not cod or not cant_str:
      messagebox.showwarning(
          "Atención", "Todos los campos son obligatorios.", parent=self.root
      )
      return

    try:
      cant = int(cant_str)
      if cant < 0:
        raise ValueError()
    except ValueError:
      messagebox.showerror(
          "Error",
          "La cantidad debe ser un número entero mayor o igual a 0.",
          parent=self.root,
      )
      return

    estado = "Disponible" if cant > 0 else "Agotado"
    exito = self.model.agregar_producto(
        nom, cod, f"Producto {nom}", cant, estado
    )

    if exito:
      messagebox.showinfo(
          "Éxito",
          f"Producto '{nom}' guardado correctamente.",
          parent=self.root,
      )
      self.entry_nombre.delete(0, tk.END)
      self.entry_codigo.delete(0, tk.END)
      self.entry_cantidad.delete(0, tk.END)
      self._cargar_productos()
    else:
      messagebox.showerror(
          "Error",
          "No se pudo registrar en la base de datos.",
          parent=self.root,
      )