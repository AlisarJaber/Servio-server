from models.cart import Cart
from data.products import products
carts = [
    Cart(
        id=1,
        customerName="Alisar",
        productIds=[1,2,3],
        isPaid=False
    ),
    Cart(
        id=2,
        customerName="Noor",
        productIds=[2, 4],
        isPaid=True
    ),
    Cart(
        id=3,
        customerName="Mais",
        productIds=[],
        isPaid=False
    )
]

