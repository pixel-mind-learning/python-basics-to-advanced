from pydantic import BaseModel


class Address(BaseModel):
    street: str
    city: str
    state: str
    zip: int
    country: str


class User(BaseModel):
    id: int
    firstName: str
    lastName: str
    address: Address


address = Address(
    street="123 Main St", city="Anytown", state="CA", zip=12345, country="USA"
)

user = User(id=1, firstName="maleesha", lastName="sandakalum", address=address)

print(user)
