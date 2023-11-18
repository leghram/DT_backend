from pydantic import BaseModel, ConfigDict
from typing import Optional


class BaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class UserAuth(BaseSchema):
    username: str
    password: str


class User(BaseSchema):
    id: Optional[int] = None
    nombre: str
    apellido: str
    username: str


class UserLogin(User):
    password: str


class UserDB(User):
    hash_password: str
