class ProductNotFoundError(Exception):
    pass


def get_product(product_id):
    product = None

    if product is None:
        raise ProductNotFoundError(f"Product {product_id} not found")

    return product


import pytest


def test_product_not_found():
    with pytest.raises(
        ProductNotFoundError,
        match="Product 101 not found",
    ):
        get_product(101)
