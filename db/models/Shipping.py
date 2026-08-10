from typing import Optional

from sqlmodel import SQLModel, Field, Relationship
from enum import Enum

class ShippingState(str, Enum):
    PENDING = "pending"
    ASSIGNED = "assigned"
    DELIVERED = "delivered"
class Shipping(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    origin: str
    destination: str
    weight: float
    hour: float
    state: ShippingState = Field(default= ShippingState.PENDING)
    truck_id: int = Field(foreign_key="truck.id")
    truck = Relationship(back_populates="shipment")
