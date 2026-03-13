# SOLICITAR DATOS AL USUARIO
nombre_del_producto = input("Enter your product name: ")

try:
    precio = float(input("Enter the price: ").replace(",", "."))
    cantidad = int(input("How many products?: "))
except ValueError:
    print("Invalid input. Please enter numbers only.")
    
    precio = float(input("Enter the price: ").replace(",", "."))
    cantidad = int(input("How many products?: "))

costo_total = precio * cantidad

# RESTRICCION DE DATOS INVALIDOS
if precio <= 0:
    print("Enter a valid number.")
elif cantidad <= 0:
    print("Enter a correct number")

# MUESTRA DE RESULTADO EN PANTALLA
else:
    print(
        f"\nProduct name: {nombre_del_producto}\n"
        f"Price: {precio}\n"
        f"Quantity: {cantidad}\n"
        f"Total cost: {costo_total}\n"
        f"Thanks for your purchase!"
    )