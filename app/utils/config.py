import os

from dotenv import load_dotenv

load_dotenv()


class DB_CONFIG:
    @staticmethod
    def get_username():
        return os.getenv("DB_USERNAME")

    @staticmethod
    def get_password():
        return os.getenv("DB_PASSWORD")

    @staticmethod
    def get_host():
        return os.getenv("DB_HOST")

    @staticmethod
    def get_database_name():
        return os.getenv("DB_DATABASE_NAME")

    @staticmethod
    def get_port():
        return os.getenv("DB_PORT")


class TOKEN_CONFIG:
    @staticmethod
    def get_secret_key():
        return os.getenv("API_SECRET_KEY")

    @staticmethod
    def get_algorithm():
        return os.getenv("API_ALGORITHM")
