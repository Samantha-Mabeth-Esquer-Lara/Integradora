# database_connection.py
from config import DB_CONFIG


class DatabaseConnection:

  def __init__(self):
    self.config = DB_CONFIG

  def get_connection(self):
    try:
      import psycopg2

      return psycopg2.connect(**self.config)
    except Exception as e:
      print(f"[Aviso BD]: {e}")
      return None

  def consultar(self, query, params=()):
    conexion = self.get_connection()
    if not conexion:
      return None
    try:
      cursor = conexion.cursor()
      cursor.execute(query, params)
      columnas = [col[0] for col in cursor.description]
      resultados = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
      cursor.close()
      conexion.close()
      return resultados
    except Exception as e:
      print(f"Error en consulta: {e}")
      return None

  def ejecutar(self, query, params=()):
    conexion = self.get_connection()
    if not conexion:
      return False
    try:
      cursor = conexion.cursor()
      cursor.execute(query, params)
      conexion.commit()
      cursor.close()
      conexion.close()
      return True
    except Exception as e:
      print(f"Error al ejecutar: {e}")
      return False