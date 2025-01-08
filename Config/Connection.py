import mysql.connector
from mysql.connector import Error

class database:
    try:
        connection= mysql.connector.connect(user="root",
                                        password="12345678",
                                        host="localhost",
                                        database="sistemas_alquiler",
                                        port="3306")

    except Error as e:
        print(f"Error al conectar con la base de datos: {e}")