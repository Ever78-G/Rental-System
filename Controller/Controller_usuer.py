
from Configuracion.Conexion import Database
from Model.User import User

class ControllerUser:
    
    db = Database()

    def __init__(self, user):
        self.user = user

    def login(self):

        try:
            bd=Database()

            # Consulta SQL para verificar usuario
            query = "SELECT * FROM usuario WHERE user = %s"
            valor = (self.user.usuario,)  # Asegúrate de que sea una tupla
            consulta = bd.fetch_query(query,valor)
            return consulta
        
        
        except Exception as e:
            # Manejo de errores
            print(f"Error durante el login: {e}")
            return None
    
    

    
