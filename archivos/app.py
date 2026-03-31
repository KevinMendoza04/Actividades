from servicios import (
    agregar_producto,
    mostrar_inventario,
    buscar_producto,
    actualizar_producto,
    eliminar_producto,
    calcular_estadisticas,
)
from archivos import guardar_csv, cargar_csv, fusionar_inventario



#  Inventario global en memoria (lista de dicts)

inventario = []


#  Helpers de entrada segura


def pedir_float(mensaje):
    """
    Solicita un número flotante no negativo al usuario.

    Parámetros:
        mensaje (str): Texto del prompt.

    Retorno:
        float: Valor ingresado y validado.
    """
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("  ⚠  El valor no puede ser negativo.")
                continue
            return valor
        except ValueError:
            print("  ⚠  Ingrese un número válido.")


def pedir_int(mensaje):
    """
    Solicita un número entero no negativo al usuario.

    Parámetros:
        mensaje (str): Texto del prompt.

    Retorno:
        int: Valor ingresado y validado.
    """
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("  ⚠  El valor no puede ser negativo.")
                continue
            return valor
        except ValueError:
            print("  ⚠  Ingrese un número entero válido.")


def pedir_ruta(operacion="guardar"):
    """
    Solicita una ruta de archivo al usuario.

    Parámetros:
        operacion (str): 'guardar' o 'cargar', para el mensaje de ayuda.

    Retorno:
        str: Ruta ingresada por el usuario.
    """
    ejemplo = "inventario.csv" if operacion == "guardar" else "inventario.csv"
    ruta = input(f"  Ingrese la ruta del archivo CSV (ej: {ejemplo}): ").strip()
    if not ruta:
        ruta = ejemplo
        print(f"  ℹ  Se usará la ruta por defecto: '{ruta}'")
    return ruta



#  Handlers de cada opción del menú


def menu_agregar():
    """Solicita datos y agrega un nuevo producto al inventario."""
    print("\n─── Agregar producto ───")
    nombre = input("  Nombre del producto: ").strip()
    if not nombre:
        print("  ⚠  El nombre no puede estar vacío.")
        return
    precio = pedir_float("  Precio unitario: $")
    cantidad = pedir_int("  Cantidad: ")
    agregar_producto(inventario, nombre, precio, cantidad)


def menu_mostrar():
    """Muestra todos los productos del inventario."""
    print("\n─── Inventario actual ───")
    mostrar_inventario(inventario)


def menu_buscar():
    """Busca un producto por nombre y muestra su información."""
    print("\n─── Buscar producto ───")
    nombre = input("  Nombre a buscar: ").strip()
    producto = buscar_producto(inventario, nombre)
    if producto:
        print(f"\n  ✔  Encontrado:")
        print(f"     Nombre  : {producto['nombre']}")
        print(f"     Precio  : ${producto['precio']:.2f}")
        print(f"     Cantidad: {producto['cantidad']}")
    else:
        print(f"  ✖  Producto '{nombre}' no encontrado.")


def menu_actualizar():
    """Actualiza precio y/o cantidad de un producto existente."""
    print("\n─── Actualizar producto ───")
    nombre = input("  Nombre del producto a actualizar: ").strip()

    producto = buscar_producto(inventario, nombre)
    if not producto:
        print(f"  ✖  Producto '{nombre}' no encontrado.")
        return

    print(f"  Producto actual → precio: ${producto['precio']:.2f}, "
          f"cantidad: {producto['cantidad']}")
    print("  (Presione Enter para dejar el valor sin cambios)")

    # Precio
    precio_str = input("  Nuevo precio: $").strip()
    nuevo_precio = float(precio_str) if precio_str else None
    if nuevo_precio is not None and nuevo_precio < 0:
        print("  ⚠  Precio inválido, no se actualizará.")
        nuevo_precio = None

    # Cantidad
    cantidad_str = input("  Nueva cantidad: ").strip()
    nueva_cantidad = None
    if cantidad_str:
        try:
            nueva_cantidad = int(cantidad_str)
            if nueva_cantidad < 0:
                print("  ⚠  Cantidad inválida, no se actualizará.")
                nueva_cantidad = None
        except ValueError:
            print("  ⚠  Cantidad inválida, no se actualizará.")

    actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad)


def menu_eliminar():
    """Elimina un producto del inventario previa confirmación."""
    print("\n─── Eliminar producto ───")
    nombre = input("  Nombre del producto a eliminar: ").strip()

    producto = buscar_producto(inventario, nombre)
    if not producto:
        print(f"  ✖  Producto '{nombre}' no encontrado.")
        return

    confirmar = input(f"  ¿Confirma eliminar '{nombre}'? (S/N): ").strip().upper()
    if confirmar == "S":
        eliminar_producto(inventario, nombre)
    else:
        print("  ℹ  Eliminación cancelada.")


def menu_estadisticas():
    """Calcula y muestra estadísticas del inventario."""
    calcular_estadisticas(inventario)


def menu_guardar_csv():
    """Guarda el inventario en un archivo CSV."""
    print("\n─── Guardar CSV ───")
    ruta = pedir_ruta("guardar")
    guardar_csv(inventario, ruta)


def menu_cargar_csv():
    """
    Carga productos desde un CSV, permitiendo sobrescribir o fusionar
    con el inventario actual.
    """
    global inventario
    print("\n─── Cargar CSV ───")
    ruta = pedir_ruta("cargar")

    # Intentar leer el archivo
    productos_cargados, filas_invalidas = cargar_csv(ruta)

    if productos_cargados is None:
        # Error crítico ya reportado dentro de cargar_csv
        return

    if not productos_cargados:
        print(f"  ⚠  No se encontraron filas válidas en '{ruta}'.")
        if filas_invalidas:
            print(f"  ℹ  {filas_invalidas} fila(s) inválida(s) omitida(s).")
        return

    # Preguntar acción: sobrescribir o fusionar
    print(f"\n  Se cargaron {len(productos_cargados)} producto(s) válido(s) "
          f"(filas inválidas: {filas_invalidas}).")
    accion = input("  ¿Sobrescribir inventario actual? (S/N): ").strip().upper()

    if accion == "S":
        # Reemplazar inventario completo
        inventario = productos_cargados
        print(f"\n  ✔  Inventario reemplazado con {len(inventario)} producto(s).")
        accion_texto = "Reemplazo total"
    else:
        # Fusionar con el inventario existente
        agregados, actualizados = fusionar_inventario(inventario, productos_cargados)
        print(f"\n  ✔  Fusión completada: {agregados} producto(s) nuevo(s), "
              f"{actualizados} actualizado(s).")
        accion_texto = "Fusión"

    # Resumen final
    print("\n  ─── Resumen de carga ───")
    print(f"  Productos cargados del CSV : {len(productos_cargados)}")
    print(f"  Filas inválidas omitidas   : {filas_invalidas}")
    print(f"  Acción aplicada            : {accion_texto}")
    print(f"  Inventario actual          : {len(inventario)} producto(s)\n")

    # Mostrar inventario actualizado
    mostrar_inventario(inventario)


#  Menú principal

OPCIONES = {
    "1": ("Agregar producto",    menu_agregar),
    "2": ("Mostrar inventario",  menu_mostrar),
    "3": ("Buscar producto",     menu_buscar),
    "4": ("Actualizar producto", menu_actualizar),
    "5": ("Eliminar producto",   menu_eliminar),
    "6": ("Estadísticas",        menu_estadisticas),
    "7": ("Guardar CSV",         menu_guardar_csv),
    "8": ("Cargar CSV",          menu_cargar_csv),
    "9": ("Salir",               None),
}


def mostrar_menu():
    """Imprime el menú principal de opciones."""
    print("\n" + "╔" + "═" * 37 + "╗")
    print("║    🗃  SISTEMA DE INVENTARIO  🗃     ║")
    print("╠" + "═" * 37 + "╣")
    for num, (desc, _) in OPCIONES.items():
        print(f"║  {num}.  {desc:<30} ║")
    print("╚" + "═" * 37 + "╝")


def main():
    """Bucle principal del programa. Mantiene el menú activo hasta 'Salir'."""
    print("\n  Bienvenido al Sistema de Inventario Avanzado")

    while True:
        mostrar_menu()
        opcion = input("\n  Seleccione una opción (1-9): ").strip()

        if opcion not in OPCIONES:
            print("  ⚠  Opción inválida. Ingrese un número del 1 al 9.")
            continue

        descripcion, handler = OPCIONES[opcion]

        # Opción Salir
        if opcion == "9":
            print("\n  👋  ¡Hasta luego! Cerrando el sistema...\n")
            break

        # Ejecutar el handler protegido por try/except para no cerrar el programa
        try:
            handler()
        except KeyboardInterrupt:
            print("\n  ℹ  Operación cancelada por el usuario.")
        except Exception as e:
            print(f"\n  ✖  Error inesperado en '{descripcion}': {e}")
            print("  ℹ  Volviendo al menú principal...")


if __name__ == "__main__":
    main()
