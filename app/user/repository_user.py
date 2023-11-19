from app.conection.db_client_provider import SesionProvider

from app.user.model_user import User

session = SesionProvider()


class UserRepository:
    def __init__(self, session=session):
        try:
            self.__session = session
        except Exception:
            raise

    def read(self):
        try:
            users = self.__session.query(User).all()
            return users
        except Exception:
            raise

    def create(self, user: User):
        try:
            self.__session.add(user)
            self.__session.commit()
            self.__session.refresh(user)
            return user
        except Exception:
            raise

    def update(self, user: User):
        try:
            self.__session.add(user)
            self.__session.commit()
            self.__session.refresh(user)
            return user
        except Exception:
            raise

    def remove(self, user):
        try:
            self.__session.delete(user)
            self.__session.commit()
        except Exception:
            raise

    def read_last(self):
        try:
            user = self.__session.query(User).order_by(User.id.desc()).first()
            return user
        except Exception:
            raise

    def read_user_by_username(self, username):
        try:
            user = self.__session.query(User).filter(User.username == username).first()
            return user
        except Exception:
            raise

    def read_user_by_id(self, id):
        try:
            user = self.__session.query(User).filter(User.id == id).first()
            return user
        except Exception:
            raise
