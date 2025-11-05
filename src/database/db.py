from peewee import *
import os
from pathlib import Path

# Configuración de rutas multiplataforma
def get_db_path():
    """Obtiene la ruta de la BD según la plataforma"""
    if hasattr(os, 'getuid'):  # Linux/Mac
        base_dir = Path.home() / '.mi_app'
    else:  # Windows
        base_dir = Path.home() / 'AppData' / 'Local' / 'Rental_system'
    
    base_dir.mkdir(parents=True, exist_ok=True)
    
    return base_dir / 'renta.db'

# Conexión global a la BD
database = SqliteDatabase(get_db_path())

class BaseModel(Model):
    """Modelo base que todos los modelos heredarán"""
    class Meta:
        database = database

# Singleton para manejar la conexión
class DatabaseManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.initialized = False
        return cls._instance
    
    def initialize(self):
        """Inicializa la BD y crea tablas"""
        if not self.initialized:
            self.connect()
            self.create_tables()
            self.initialized = True
    
    def connect(self):
        """Conecta a la BD"""
        database.connect()
    
    def close(self):
        """Cierra la conexión"""
        if not database.is_closed():
            database.close()
    
    def create_tables(self):
        """Crea todas las tablas definidas en modelos"""
        from database.models.user import User
        
        tables = [User]
        database.create_tables(tables, safe=True)
    
    def get_db(self):
        """Retorna la instancia de la BD para usar en cualquier lugar"""
        return database

# Instancia global
db_manager = DatabaseManager()