from passlib.context import CryptContext
from app.user.repository_user import UserRepository
from app.user.schema_user import User as UserSchema
from app.user.schema_user import UserLogin
from app.user.schema_user import UserDB
from app.user.model_user import User as UserModel


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hashed(password):
    return pwd_context.hash(password)


class UserService:
    def __init__(self, repository: UserRepository):
        self.__repository = repository

    def get(self):
        users = self.__repository.read()
        users_mapped = [UserSchema.model_validate(user) for user in users]
        return users_mapped

    def add(self, user: UserLogin):
        user_db = UserDB(**user.__dict__, hash_password="")
        user_db.hash_password = get_password_hashed(user.password)
        user_model = UserModel(**user_db.__dict__)
        self.__repository.create(user_model)
        user_created = UserSchema.model_validate(self.__repository.read_last())
        return user_created
