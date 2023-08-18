from db.models.main import BaseModel

def main():
  print(BaseModel._meta.database.get_tables())


if __name__ == '__main__':
  main()
