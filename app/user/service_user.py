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

    def get_by_username(self, username, password):
        user_db = self.__repository.read_user_by_username(username)
        if user_db is None:
            return None
        if user_db.username == username and pwd_context.verify(password, user_db.hash_password):
            return UserSchema.model_validate(user_db)
        return None

    def add(self, user: UserLogin):
        user_db = UserDB(**user.__dict__, hash_password="")
        user_db.hash_password = get_password_hashed(user.password)
        user_model = UserModel(**user_db.__dict__)
        self.__repository.create(user_model)
        user_created = UserSchema.model_validate(self.__repository.read_last())
        return user_created

    def update(self, id, user):
        current_user = self.__repository.read_user_by_id(id)
        if current_user is None:
            return
        for key, value in user.__dict__.items():
            if value is None:
                continue
            setattr(current_user, key, value)
        user_updated = self.__repository.update(current_user)
        return UserSchema.model_validate(user_updated)

    def delete(self, user_id):
        user_db = self.__repository.read_user_by_id(user_id)
        if user_db is None:
            return None
        self.__repository.remove(user_db)
        return {"status": "success"}

    def get_by_id(self, id: int):
        user_db = self.__repository.read_user_by_id(id)
        if user_db is None:
            return None
        return UserSchema.model_validate(user_db)
