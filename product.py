class Product:
    def __init__(self, name : str, price : float, quantity : int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def check_quantity(self) -> bool:
        return self.quantity >= 10

    def display_info(self) -> str:
        return f'Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}'
