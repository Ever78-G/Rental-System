import tkinter as tk
from View.BasicView import UI
from Controller.Controller_usuer import ControllerUser
from Model.User import User
from Configuracion.Conexion import Database



class login(UI):
    def init_ui(self):
        super().init_ui()

        # Crear un Frame con configuración de tamaño y color
        frame = tk.Frame(self.parent)
        frame.configure(width=521, height=545, bg="#080A2C", borderwidth=5, relief="sunken")
        frame.pack_propagate(False)  # Esto asegura que el frame mantenga el tamaño especificado
        frame.pack(pady=100)

        titule = tk.Label(frame, text="Renta System", fg="#1B984D",bg="#080A2C" ,font=("Spicy Rice", 20))
        titule.pack(pady=20)  
        loginbutton= tk.Button(frame,text="login", width=50,height=2)
        loginbutton.place(y=320,x=80)

    def inicio():
                root = tk.Tk()
                app = login(parent=root, bg_color="#0C083B")  # Fondo de la ventana
                app.mainloop()

                db = Database()

                print("Conexión a la base de datos establecida:", db)
                prunda=User("ever","5421212")
                # Crear una instancia de usuario controlador
                usuario = ControllerUser(prunda)
                
                # Realizar login
                resultado = usuario.login()
                print("Resultado del login:", resultado)

    
                

    



