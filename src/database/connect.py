import pyodbc
from config.settings import settings

def get_connection():
  """
  Cria e retorna uma conexão com o banco de dados
  """
  conn_str = f'DRIVER={settings.DB_DRIVER};SERVER={settings.DB_SERVER};DATABASE={settings.DB_DATABASE};UID={settings.DB_USERNAME};PWD={settings.DB_PASSWORD}'

  return pyodbc.connect(conn_str)