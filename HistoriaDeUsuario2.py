# Lista principal donde se guardan los productos
inventario = []

# FUNCION: AGREGAR PRODUCTO
def agregar_producto():
    print("\n--- AGREGAR PRODUCTO ---")
    
    nombre = input("Ingrese el nombre del producto: ").strip()
    
    # Validación de precio
    validacion = "si"
    while validacion == "si":
        try:
            precio = float(input("Ingrese el precio del producto: "))
            if precio < 0:
                print("El precio no puede ser negativo.")
                continue
            else:
                validacion = "no"
        except ValueError:
            print("Ingrese un número válido.")

    # Validación de cantidad
    validacion1 = "si"
    while validacion1 == "si":
        try:
            cantidad = int(input("Ingrese la cantidad: "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa.")
                continue
            validacion1 = "no"
        except ValueError:
            print("Ingrese un número entero válido.")

    # Crear producto como diccionario
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    # Agregar a la lista inventario
    inventario.append(producto)

    print("Producto agregado correctamente.")


# FUNCION: MOSTRAR INVENTARIO

def mostrar_inventario():
    print("\n--- INVENTARIO ---")

    # Validar si está vacío
    if len(inventario) == 0:
        print("El inventario está vacío.")
        return

    # Recorrer con for
    for producto in inventario:
        print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")


# FUNCION: CALCULAR ESTADISTICAS
def calcular_estadisticas():
    print("\n--- ESTADÍSTICAS ---")

    if len(inventario) == 0:
        print("No hay productos para calcular.")
        return

    valor_total = 0
    total_productos = 0

    # Recorrer inventario
    for producto in inventario:
        valor_total += producto["precio"] * producto["cantidad"]
        total_productos += producto["cantidad"]

    print(f"Valor total del inventario: {valor_total}")
    print(f"Cantidad total de productos: {total_productos}")



# MENU PRINCIPAL
def menu():
    variable_si = "si"
    while variable_si == "si":
        print("\n===== MENÚ INVENTARIO =====")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Calcular estadísticas")
        print("4. Salir")

        opcion = input("Seleccione una opción: ").strip()

        # Control de flujo
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            calcular_estadisticas()
        elif opcion == "4":
            print("Saliendo del programa...")
            variable_si = "no"
        else:
            print("Opción inválida. Intente nuevamente.")


# ------------------------------
# EJECUCION DEL PROGRAMA
# ------------------------------
menu()
