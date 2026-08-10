from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from db.models.Shipping import Shipping

class Truck(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    capacity: float
    originCity: str
    fuel: float
    alpha: float
    beta: float
    startHour: float
    finishHour: float
    active: bool = Field(default=False)
    driver_id: Optional[int] = Field(default= None, foreign_key="user.id")
    driver = Relationship(back_populates="trucks")
    shipment: list[Shipping] = Relationship()