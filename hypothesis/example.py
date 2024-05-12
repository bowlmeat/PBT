from hypothesis import given, strategies as st

class Product:
    def __init__(self, price: float) -> None:
        self.price: float = price
    
    def get_discount_price(self, discount_percentage: float):
        return self.price * (discount_percentage / 100)
    

@given(
    price = st.floats(min_value=0, allow_nan=False, allow_infinity=False),
    discount_percentage=st.floats(
        min_value=0, max_value=100, allow_nan=False, allow_infinity=False
    ),
)
def test(price, discount_percentage):
    product = Product(price)
    assert product.get_discount_price(discount_percentage) <= product.price