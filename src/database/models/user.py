from peewee import *
from database.db import BaseModel

class User(BaseModel):
    username =CharField(unique= True,max_length=50)
    password = CharField(max_length=60)
    
    def to_dict(self):
        """Convierte el modelo a diccionario para fácil uso en Flet"""
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,

        }
    
    class Meta:
        table_name = 'users'