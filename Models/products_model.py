# products_model.py
from database_connection import DatabaseConnection


class SistemaModel:

  def __init__(self):
    self.db = DatabaseConnection()

  def autenticar(self, usuario, contrasena):
    query = """
            SELECT username, "role" 
            FROM stationary.users 
            WHERE LOWER(username) = LOWER(%s) AND password = %s;
        """
    resultado = self.db.consultar(query, (usuario, contrasena))
    if resultado:
      return resultado[0]

    # Respaldo offline de prueba
    usuarios_locales = {
        "samantha": ("abcd", "Administrador"),
        "claudio": ("1234", "Administrador"),
        "sergio": ("sergio123", "Administrador"),
        "brandon": ("admin123", "Administrador"),
        "oscar": ("pass123", "Empleado"),
    }
    user_key = usuario.lower().strip()
    if (
        user_key in usuarios_locales
        and usuarios_locales[user_key][0] == contrasena
    ):
      return {"username": usuario, "role": usuarios_locales[user_key][1]}
    return None

  def obtener_productos(self):
    query = """
            SELECT id_product, name, code, quantity, state 
            FROM stationary.products 
            ORDER BY id_product ASC;
        """
    resultado = self.db.consultar(query)
    if resultado is not None:
      return resultado

    # Respaldo por si la BD no está disponible
    return [
        {
            "id_product": 1,
            "name": "Cuaderno",
            "code": "PRD-101",
            "quantity": 15,
            "state": "Disponible",
        },
        {
            "id_product": 2,
            "name": "Lapiz",
            "code": "PRD-102",
            "quantity": 0,
            "state": "Agotado",
        },
        {
            "id_product": 3,
            "name": "Borrador",
            "code": "PRD-103",
            "quantity": 25,
            "state": "Disponible",
        },
    ]

  def agregar_producto(self, nombre, codigo, descripcion, cantidad, estado):
    query = """
            INSERT INTO stationary.products (name, code, description, quantity, state) 
            VALUES (%s, %s, %s, %s, %s);
        """
    return self.db.ejecutar(query, (nombre, codigo, descripcion, cantidad, estado))