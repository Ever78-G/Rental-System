import bcrypt


class User:
    def __init__(self,user,password=None):
        self.usuario=user
        self.__password=password

    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self,password):
        password_bytes=password.encode('utf-8')
        salt = bcrypt.gensalt()
        password_cifrar=bcrypt.hashpw(password_bytes,salt)
        self.__password= password_cifrar

    def verificar_password(self, password):
        password_bytes = password.encode('utf-8')
        return bcrypt.checkpw(password_bytes, self.__password)


usuario= User("ever",b'$2b$12$0J5VVd/dS8OkOqIVuWKxoO5.iSme.ycCx9RygwgsR4XuvPgMD07MC')

print(usuario.verificar_password("ever"))