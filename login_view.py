# login_view.py
import tkinter as tk
from tkinter import messagebox
from home_view import DashboardVentana
from products_model import SistemaModel


class LoginVentana:

  def __init__(self, root):
    self.root = root
    self.root.title("Acceso al Sistema - Papelería")
    self.root.geometry("340x350")
    self.root.resizable(False, False)
    self.root.configure(bg="#212124")

    self.model = SistemaModel()
    self._crear_interfaz()

  def _crear_interfaz(self):
    lbl_titulo = tk.Label(
        self.root,
        text="Iniciar Sesión",
        font=("Helvetica", 15, "bold"),
        fg="#ffffff",
        bg="#212124",
    )
    lbl_titulo.pack(pady=(30, 20))

    lbl_usuario = tk.Label(
        self.root,
        text="Usuario:",
        font=("Helvetica", 10),
        fg="#cfcfcf",
        bg="#212124",
    )
    lbl_usuario.pack(anchor="w", padx=35, pady=(5, 2))
    self.entry_usuario = tk.Entry(
        self.root,
        font=("Helvetica", 10),
        bg="#141416",
        fg="#ffffff",
        insertbackground="white",
    )
    self.entry_usuario.pack(fill="x", padx=35, ipady=3)
    self.entry_usuario.insert(0, "Samantha")

    lbl_pass = tk.Label(
        self.root,
        text="Contraseña:",
        font=("Helvetica", 10),
        fg="#cfcfcf",
        bg="#212124",
    )
    lbl_pass.pack(anchor="w", padx=35, pady=(12, 2))
    self.entry_pass = tk.Entry(
        self.root,
        show="*",
        font=("Helvetica", 10),
        bg="#141416",
        fg="#ffffff",
        insertbackground="white",
    )
    self.entry_pass.pack(fill="x", padx=35, ipady=3)
    self.entry_pass.insert(0, "abcd")

    btn_entrar = tk.Button(
        self.root,
        text="Entrar",
        font=("Helvetica", 10, "bold"),
        bg="#ffffff",
        fg="#000000",
        relief="flat",
        cursor="hand2",
        command=self._iniciar_sesion,
    )
    btn_entrar.pack(fill="x", padx=35, pady=(25, 0), ipady=4)

  def _iniciar_sesion(self):
    usuario = self.entry_usuario.get().strip()
    contra = self.entry_pass.get().strip()

    if not usuario or not contra:
      messagebox.showwarning(
          "Atención", "Ingresa usuario y contraseña.", parent=self.root
      )
      return

    datos_usuario = self.model.autenticar(usuario, contra)
    if datos_usuario:
      self.root.destroy()
      dashboard_root = tk.Tk()
      DashboardVentana(
          dashboard_root,
          usuario_activo=datos_usuario["username"],
          rol_activo=datos_usuario["role"],
      )
      dashboard_root.mainloop()
    else:
      messagebox.showerror(
          "Error", "Usuario o contraseña incorrectos.", parent=self.root
      )