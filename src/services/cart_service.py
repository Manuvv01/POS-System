from src.models.cart import Cart

def load_Cart(product_obj, cart):
    """
    Adds the Products in the Cart

    :param:
        product_obj (Product): Product class object
    :param:
        cart (Cart): Cart class object
    :return:
    """
    cart.add_item(product= product_obj)
    print(cart.items)
    print(f"Length:  {len(cart.items)}")