class Cart:
    """
    Represents a shopping cart in the POS system.

    Stores a collection of products selected for purchase and provides
    functionality to add items and calculate the total price.

    Attributes:
        items (list): A list of products added to the cart.
    """
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def get_total(self):
        return sum(p.price for p in self.items)