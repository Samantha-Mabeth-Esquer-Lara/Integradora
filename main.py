# main.py
import tkinter as tk
from login_view import LoginVentana

if __name__ == "__main__":
  app_root = tk.Tk()
  LoginVentana(app_root)
  app_root.mainloop()