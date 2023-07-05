from functools import lru_cache

from .schema import Customer, Order, Product

CUSTOMERS: dict[int, Customer] = {}
ORDERS: dict[int, Order] = {}
PRODUCTS: dict[int, Product] = {}

@lru_cache(maxsize=1)
def get_customers_storage() -> dict[int, Customer]:
    return CUSTOMERS


@lru_cache(maxsize=1)
def get_orders_storage() -> dict[int, Order]:
    return ORDERS


@lru_cache(maxsize=1)
def get_products_storage() -> dict[int, Product]:
    return PRODUCTS