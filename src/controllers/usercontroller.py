from database.models.user import User
import bcrypt
from typing import List, Optional, Tuple

class UserController:
    
    @staticmethod
    def Get_pk(user_id: int) -> Optional[User]:
        try:
            return User.get(User.id == user_id)
        except User.DoesNotExist:
            return None

    def Get_all(self) -> List[User]:
        return list(User.select())

    def Create(self, username: str, password: str) -> Tuple[Optional[User], str]:
        try:
            # Verificar si usuario ya existe
            if User.select().where(User.username == username).exists():
                return None, "El usuario ya existe"
            
            password_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
            user = User.create(
                username=username,
                password=password_hash.decode("utf-8")
            )
            return user, "Usuario creado exitosamente"
            
        except Exception as e:
            return None, f"Error al crear usuario: {e}"

    def Update(self, user_id: int, **kwargs) -> Tuple[Optional[User], str]:
        try:
            user = self.Get_pk(user_id)
            if not user:
                return None, "Usuario no encontrado"
            
            if 'password' in kwargs:
                kwargs['password'] = bcrypt.hashpw(
                    kwargs['password'].encode(), 
                    bcrypt.gensalt()
                ).decode()
            
            # Actualizar campos
            for key, value in kwargs.items():
                setattr(user, key, value)
            
            user.save()
            return user, "Usuario actualizado exitosamente"
            
        except Exception as e:
            return None, f"Error al actualizar usuario: {e}"

    def Authenticate(self, username: str, password: str) -> Optional[User]:
        try:
            user = User.get(User.username == username)
            if bcrypt.checkpw(password.encode("utf-8"), user.password.encode("utf-8")):
                return user
            return None
        except User.DoesNotExist:
            return None