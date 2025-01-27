import mysql.connector
"""
class Database:
    def __init__(self):
        self.config = {
            'host': 'localhost',
            'user': 'root',
            'password': '12345678',
            'database': 'sistema_alquiler'
        }

    def get_connection(self):
        try:
            connection = mysql.connector.connect(**self.config)
            return connection 
        except mysql.connector.Error as e:
            print(f"Error al conectar con la base de datos: {e}")
            return None


"""

import mysql.connector
from mysql.connector import Error

import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self, host='localhost', user='root', password='12345678', database='sistema_alquiler'):
        self.config = {
            'host': host,
            'user': user,
            'password': password,
            'database': database
        }
        self.connection = None

    def get_connection(self):
        if self.connection is None or not self.connection.is_connected():
            try:
                self.connection = mysql.connector.connect(**self.config)
                print("Conexión a la base de datos exitosa")
            except Error as e:
                print(f"Error al conectar con la base de datos: {e}")
                return None
        return self.connection

    def close_connection(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexión cerrada")

    def __enter__(self):
        self.get_connection()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close_connection()

    # Método para ejecutar consultas que no devuelven datos (INSERT, UPDATE, DELETE)
    def execute_query(self, query, params=None):
        connection = self.get_connection()
        if connection:
            with connection.cursor() as cursor:
                try:
                    cursor.execute(query, params)
                    connection.commit()
                    print("Consulta ejecutada con éxito")
                except Error as e:
                    print(f"Error al ejecutar la consulta: {e}")
                    connection.rollback()  # Revertir cambios en caso de error
                finally:
                    pass  # El cursor se cierra automáticamente con `with`

    # Método para ejecutar consultas que devuelven datos (SELECT)
    def fetch_query(self, query, params=None):
        connection = self.get_connection()
        if connection:
            with connection.cursor() as cursor:
                try:
                    cursor.execute(query, params)
                    resultados = cursor.fetchall()  # Recuperar todos los datos
                    return resultados
                except Error as e:
                    print(f"Error al ejecutar la consulta: {e}")
                    return None
                finally:
                    pass  # El cursor se cierra automáticamente con `with`
