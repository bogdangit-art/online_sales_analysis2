from product import Product
from productmanager import ProductManager
from cart import Cart

if __name__ == "__main__":
    products = [
        Product("Ochelari", 589.99, 1789),
        Product("Stilou", 124.49, 234),
        Product("Carte electronica", 44.45, 0),
        Product("Vioara acustica", 325.80, 765),
        Product("Boxa", 105, 100)
    ]

    product_manager = ProductManager()

    for product in products:
        product_manager.add_product(product)

    cart = Cart()

    add_1 = cart.add_product("Ochelari", 4, product_manager)
    print(f"Succes in adaugarea ochelarilor?{add_1}")
    add_2 = cart.add_product("Carte electronica", 2, product_manager)
    print(f"Succes in adaugarea produselor carti electronice?{add_2}")

    print(f"Total cart price is:", cart.total_price())
    print(f"Cart items are:", cart.display_info())