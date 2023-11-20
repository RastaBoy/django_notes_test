from hashlib import sha256

from ..models import User
from ..dto import AuthorizationRequest, RegisterRequest

from ..exceptions import RegisterException, AuthorizationException

# Контроллер для авторизации/регистрации на сайте
# Авторизацию можно было организовать через стандартные инструменты Django,
# Но захотелось вот так :)

class AuthorizationController():
    SALT = '2gd7fjhreec5qelu'    
    
    def __generate_hash__(self, email : str, password : str) -> str:
        return sha256(f"{email}{self.SALT}{password}".encode('utf-8')).hexdigest()
    

    def register_user(self, request : RegisterRequest) -> User:
        user = User.objects.filter(email=request.email).first()
        print(user)
        if user is None:
            print('Create user!')
            return User.objects.create(
                name=request.name,
                email=request.email,
                password=self.__generate_hash__(request.email, request.password)
            )
        
        raise RegisterException(f"Пользователь с таким Email уже был зарегистрирован в системе.")
    

    ...