from app.conection.db_client_provider import SesionProvider

from app.user.model_user import User

session = SesionProvider()


class UserRepository:
    def __init__(self, session=session):
        self.__session = session

    def read(self):
        users = self.__session.query(User).all()
        return users

    def create(self, user: User):
        self.__session.add(user)
        return user

    def read_last(self):
        user = self.__session.query(User).order_by(User.id.desc()).first()
        return user
