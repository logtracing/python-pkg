import os
from peewee import Model, MySQLDatabase
from logtracing.config.database import DB_CONFIG

env = os.getenv('PYTHON_ENV', 'development')
config = DB_CONFIG[env]

database = MySQLDatabase(
    config['database'],
    **{
      'charset': 'utf8',
      'sql_mode': 'PIPES_AS_CONCAT',
      'use_unicode': True,
      'host': config['host'],
      'port': int(config['port']),
      'user': config['user'],
      'password': config['password']
      }
    )

'''
  This class is used internally by Peewee to handle 
  unknown or undefined fields within a model.
'''
class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = database
