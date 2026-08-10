from enum import Enum
from sqlmodel import Field, SQLModel, Relationship
from db.models.Truck import Truck

class UserRol(str, Enum):
    ADMIN = "admin"
    USER = "user"

class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    username: str
    password: str
    role: UserRol = Field(default=UserRol.USER)
    trucks: list[Truck] = Relationship(back_populates="driver")