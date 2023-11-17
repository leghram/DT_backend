from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker
from app.utils.config import DB_CONFIG


url_object = URL.create(
    "postgresql+pg8000",
    username=DB_CONFIG.get_username(),
    password=DB_CONFIG.get_password(),
    host=DB_CONFIG.get_host(),
    database=DB_CONFIG.get_database_name(),
    port=DB_CONFIG.get_port(),
)


class SesionProvider:
    __session = None
    __engine = None
    __sesion_maker = None

    def __new__(cls):
        if SesionProvider.__session is None:
            SesionProvider.__engine = create_engine(url_object, echo=True)
            SesionProvider.__sesion_maker = sessionmaker(bind=SesionProvider.__engine)
            SesionProvider.__session = SesionProvider.__sesion_maker()
        return SesionProvider.__session


session = SesionProvider()
