class Product:
    """
    Represents a product in the POS system.

    Attributes:
        name (str): Name of the product.
        price (float): Price of the product.
        quantity (int): Quantity in stock.
        category (str): Category of the product.
    """
    def __init__(self, name= None, price = 0.0, quantity = 0, category = None):
        """
        Initializes a Product instance.

        Args:
            name (str): Product name.
            price (float): Product price.
            quantity (int): Product stock quantity.
            category (str): Product category.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

    def __repr__(self):
        return f'Product{self.name, self.price, self.quantity, self.category}'

    def __str__(self):
        string = (f"Name: {self.name}\n"
                  f"Price: {self.price}\n"
                  f"Quantity: {self.quantity}\n"
                  f"Category: {self.category}")
        return string
