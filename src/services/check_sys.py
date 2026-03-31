"""
Sales processing module.

Handles item scanning, price calculation, total computation, and change calculation for transactions in the POS system.
"""
from src.services.spreadsheet import read_rows
from src.utils.mappers import df_to_Product
from src.models.product import Product
from src.utils.calculations import calculates_change


def check_system():
    """
    Processes a complete sales transaction.

    Includes scanning items by barcode, retrieving product data,
    calculating the total price, accepting payment, and returning change.
    """
    total_price= 0

    while True:
        barcode = int(input("Ingrese SKU(Para acabar pulsa 0): ")) #Simulates the employee scanning the item

        if barcode == 0:  #For now use this as a break statement
            break

        #Checks the item
        df_Product= read_rows("SKU", barcode)
        product= df_to_Product(df_Product, Product)

        print(f"Nombre: {product.name}, Precio: ${product.price}")
        #Gets the price
        total_price+= product.price
        #TODO: Update the quantity of the items
        print(f"Precio Total: {total_price}")
    #Ends the loop

    money = float(input("Ingresa tu dinero: "))

    change = calculates_change(total_price, money)
    print(f"Su cambio es de ${change}")

    print("Gracias por usar el sistema")
