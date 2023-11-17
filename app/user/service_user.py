from app.user.repository_user import UserRepository
from app.user.schema_user import User as UserSchema


class UserService:
    def __init__(self, repository: UserRepository):
        self.__repository = repository

    def get(self):
        users = self.__repository.read()
        users_mapped = [UserSchema.model_validate(user) for user in users]
        return users_mapped
