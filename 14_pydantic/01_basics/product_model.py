from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True


product_one = Product(id=1, name="Laptop", price="9993.99", in_stock=True)

product_two = Product(id=2, name="Mouse", price="24.33", in_stock=True)

product_three = Product(id=3, name="Keyboard")

print(product_one)