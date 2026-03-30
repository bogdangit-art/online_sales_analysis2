from product import Product

class ProductManager:
    def __init__(self):
        self.products = {}

    def total_spent(self) -> float:
        return sum(item.price * item.quantity for item in self.products)

    def add_product(self, product : Product) -> None:
        self.products[product.name] = (product.price, product.quantity)

    def display_info(self) -> str:
        return f"shopping history: {self.products}"

