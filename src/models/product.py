class Product:

    def __init__(self, name= None, price = 0.0, quantity = 0, category = None):
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
