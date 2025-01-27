# Importaciones absolutas desde los paquetes del proyecto
from View.login import login


def main():
    """"
    # Crear una conexión a la base de datos (ejemplo)
    db = Database()

    print("Conexión a la base de datos establecida:", db)
    prunda=User("ever","5421212")
    # Crear una instancia de usuario controlador
    usuario = ControllerUser(prunda)
    
    # Realizar login
    resultado = usuario.login()
    print("Resultado del login:", resultado)

    """
    login.inicio()

  

if __name__ == "__main__":
    main()

