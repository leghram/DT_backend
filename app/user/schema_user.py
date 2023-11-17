from pydantic import BaseModel, ConfigDict
from typing import Optional


class BaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class User(BaseSchema):
    id: str
    name: str
    email: str
    password: Optional[str] = ""
