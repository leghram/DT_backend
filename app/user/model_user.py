from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()
metadata = Base.metadata


class User(Base):
    """User table model representation"""

    __tablename__ = "users"
    id = Column(String(36, "utf8mb4_unicode_ci"), primary_key=True)
    name = Column(String(100, "utf8mb4_unicode_ci"), nullable=False)
    email = Column(String(100, "utf8mb4_unicode_ci"), nullable=False)
    password = Column(String(100, "utf8mb4_unicode_ci"), nullable=False)
