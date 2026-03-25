class Product:
    """
    Represents a product in the POS system.

    Attributes:
        barcode (str): Barcode of the product.
        name (str): Name of the product.
        price (float): Price of the product.
        quantity (int): Quantity in stock.
        category (str): Category of the product.
    """
    def __init__(self, barcode= None, name= None, price = 0.0, quantity = 0, category = None):
        """
        Initializes a Product instance.

        Args:
            barcode (str): Product barcode.
            name (str): Product name.
            price (float): Product price.
            quantity (int): Product stock quantity.
            category (str): Product category.
        """
        self.barcode = barcode
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

    def __repr__(self):
        return f'Product{self.barcode, self.name, self.price, self.quantity, self.category}'

    def __str__(self):
        string = (f"Barcode: {self.barcode}\n"
                  f"Name: {self.name}\n"
                  f"Price: {self.price}\n"
                  f"Quantity: {self.quantity}\n"
                  f"Category: {self.category}")
        return string

#item = Product(barcode="1254", name="Milk", price=25.0, quantity=25, category="Milks and cheese")
#item2 = Product(name="Leche", price=25.0, quantity=25, category="Milks and cheese")
