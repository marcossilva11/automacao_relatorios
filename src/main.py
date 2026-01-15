from src.database.connect import get_connection

def main():
  conn = get_connection()
  print('Conexão ok!')

if __name__ == '__main__':
  main()