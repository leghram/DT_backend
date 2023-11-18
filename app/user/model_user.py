from sqlalchemy import Column, String, BigInteger
from sqlalchemy.orm import declarative_base


Base = declarative_base()
metadata = Base.metadata


class User(Base):
    """User table model representation"""

    __tablename__ = "users"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(String(100, "utf8mb4_unicode_ci"), nullable=False)
    apellido = Column(String(100, "utf8mb4_unicode_ci"), nullable=False)
    username = Column(String(100, "utf8mb4_unicode_ci"), nullable=False)
    hash_password = Column(String(100, "utf8mb4_unicode_ci"), nullable=False)
