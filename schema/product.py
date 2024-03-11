from pydantic import BaseModel

from schema.product import Product

class Order(BaseModel):
    id: int
    customer_id: int
    items: list[int | Product]
    status: str = "pending"

class OrderCreate(BaseModel):
    customer_id: int
    items: list[int]
    status: str = "pending"

orders = [
    Order(id=1, customer_id=1, items=[1, 2], status="pending")
]