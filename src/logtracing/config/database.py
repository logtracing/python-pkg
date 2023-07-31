import os
from dotenv import load_dotenv
load_dotenv()

DB_CONFIG = {
  "development": {
    "user": os.getenv('MYSQL_USERNAME_DEV'),
    "password": os.getenv('MYSQL_PASSWORD_DEV'),
    "database": os.getenv('MYSQL_DATABASE_DEV'),
    "host": os.getenv('MYSQL_HOST_DEV'),
    "port": os.getenv('MYSQL_PORT_DEV'),
  },
  "production": {
    "user": os.getenv('MYSQL_USERNAME_PROD'),
    "password": os.getenv('MYSQL_PASSWORD_PROD'),
    "database": os.getenv('MYSQL_DATABASE_PROD'),
    "host": os.getenv('MYSQL_HOST_PROD'),
    "port": os.getenv('MYSQL_PORT_PROD'),
  },
}
