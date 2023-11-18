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
        self.__session.commit()
        self.__session.refresh(user)
        return user

    def update(self, user: User):
        self.__session.add(user)
        self.__session.commit()
        self.__session.refresh(user)
        return user

    def remove(self, user):
        self.__session.delete(user)
        self.__session.commit()

    def read_last(self):
        user = self.__session.query(User).order_by(User.id.desc()).first()
        return user

    def read_user_by_username(self, username):
        user = self.__session.query(User).filter(User.username == username).first()
        return user

    def read_user_by_id(self, id):
        user = self.__session.query(User).filter(User.id == id).first()
        return user
