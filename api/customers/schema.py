from pydantic import BaseModel


class CustomerCreateSchema(BaseModel):
    name: str
    surname: str
    email: str
    phone_number: str

    class Config:
        schema_extra = {
            "example": {
                "name": "Bartosz",
                "surname": "Sosin",
                "email": "bartek.sosin@mail.com",
                "phone_number": "123-456-789",
            }
        }


class CustomerUpdateSchema(BaseModel):
    name: str | None
    surname: str | None
    email: str | None
    phone_number: str | None

    class Config:
        schema_extra = {"example": {"name": "Bartosz", "surname": "Sosin"}}


class Customer(CustomerCreateSchema):
    id: int


class OrderCreateSchema(BaseModel):
    customer_id: int
    order_items: list[int]

    class Config:
        schema_extra = {
            "example": {
                "customer_id": 0,
                "order_items": [0, 1, 2, 3],
            }
        }


class OrderUpdateSchema(BaseModel):
    customer_id: int | None
    order_items: list[int] | None

    class Config:
        schema_extra = {
            "example": {
                "customer_id": 0,
                "order_items": [0, 1, 2, 3],
            }
        }


class Order(OrderCreateSchema):
    order_id: int


class ProductCreateSchema(BaseModel):
    name: str
    price: str
    description: str

    class Config:
        schema_extra = {
            "example": {
                "name": "Product",
                "price": "0.00$",
                "description": "Product description",
            }
        }


class ProductUpdateSchema(BaseModel):
    name: str | None
    price: str | None
    description: str | None

    class Config:
        schema_extra = {"example": {"name": "Product"}}


class Product(ProductCreateSchema):
    id: int