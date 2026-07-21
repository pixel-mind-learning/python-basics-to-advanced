from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime


class Address(BaseModel):
    street: str
    city: str
    state: str
    zip: int
    country: str


class User(BaseModel):
    id: int
    username: str
    full_name: Optional[str] = None
    email: str
    is_active: bool = True
    created_at: datetime
    address: Address
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime("%d-%m-%Y, %H:%M:%S")},
        extra="ignore",
    )


address = Address(
    street="123 Main St", city="Kandy", state="Central", zip=20000, country="Sri Lanka"
)

user = User(
    id=1,
    username="maleeshasa",
    full_name="Malisha Samarakoon",
    email="maleesha@gmail.com",
    is_active=True,
    created_at=datetime(2026, 5, 5, 5, 5, 5),
    address=address,
    tags=["premium", "subscriber"],
)

# Serialize to JSON
print("Serialized User JSON:")
print(user.model_dump_json(indent=2))


python_dict = user.model_dump()
print(python_dict)
