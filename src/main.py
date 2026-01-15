from src.database.connect import get_connection

def main():
  try:
    conn = get_connection()
    print('Conexão ok!')
  
  except Exception as e:
    print(f'Erro ao conectar: {e}')

if __name__ == '__main__':
  main()