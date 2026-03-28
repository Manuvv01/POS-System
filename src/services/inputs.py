"""
Does operations that will affect the Product object
"""

def add_by_scan(product):
    """
    Assigns the values from the user and creates a variable from the Product class
    
    :param:
        product: Product object
    :return:
        An item of a Product object
    """
    while True:
        barcode = input("Escanee el codigo de barras").strip()
        if barcode != "":
            break
        print("El codigo de barras no puede estar vacío. Intenta de nuevo.")

    while True:
        name = input("Nombre: ").strip()
        if name != "":
            break
        print("El nombre no puede estar vacío. Intenta de nuevo.")

    while True:
        try:
            price = float(input("Precio: ").strip())
            break
        except ValueError:
            print("Ingresa un número decimal para el precio.")

    while True:
        try:
            quantity = int(input("Cantidad: ").strip())
            break
        except ValueError:
            print("Ingresa un número entero válido para la cantidad.")

    category = input("Categoria (Enter para omitir): ").strip()

    if category == "":
        category = "General"

    #Creates the Product object
    item = product(barcode= barcode,name= name,price= price,quantity= quantity,category= category)
    return item

def add_by_manual(product):
    """
    Assigns the values from the user and creates a variable from the Product class

    :param:
        product: Product object
    :return:
        An item of a Product object
    """

    while True:
        name = input("Nombre: ").strip()
        if name != "":
            break
        print("El nombre no puede estar vacío. Intenta de nuevo.")

    while True:
        try:
            price = float(input("Precio: ").strip())
            break
        except ValueError:
            print("Ingresa un número decimal para el precio.")

    while True:
        try:
            quantity = int(input("Cantidad: ").strip())
            break
        except ValueError:
            print("Ingresa un número entero válido para la cantidad.")

    category = input("Categoria (Enter para omitir): ").strip()

    if category == "":
        category = "General"

    # Creates the Product object
    item = product(name= name, price= price, quantity= quantity, category= category)
    return item

def update_conditions():
    """
        Function that will update the variable object
    :param:
        product (Product): variable of class Product
    :return:
        An object of type product
    """

    #Prompt the user to get the old value
    name = input("Escriba el nombre del producto: ")
    #Prompt the user to enter the column
    column = input("Que desea cambiar(Nombre, SKU, Precio, Cantidad, Categoria): ")
    #Prompt the user to enter the new value
    new = input("Escriba el nuevo valor: ")

    #Returns the name and the parameter to be changed
    return name, column, new