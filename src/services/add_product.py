#TODO Refactor the input validation for whitespaces
def add_by_scan(product):
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

