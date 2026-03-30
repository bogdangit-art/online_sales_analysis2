from product import Product
from product_manager import ProductManager

class Cart:
    def __init__(self):
        self.cart_items = []

    def add_product(self, product_name : str, quantity: int, product_manager : ProductManager) -> bool:
         for name in product_manager.products.keys():
            if product_name == name:
                self.cart_items.append(Product(product_name, product_manager.products[name][0], quantity))
                return True
         return False

    def total_price(self) -> float:
        return sum(item.price * item.quantity for item in self.cart_items)

    def display_info(self) -> str:
        str_return = ""
        for product in self.cart_items:
            str_return += product.name + " in quantity " + str(product.quantity) + " "

        return str_return