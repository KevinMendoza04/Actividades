def agregar_producto(inventario, nombre, precio, cantidad):
    """
    Agrega un nuevo producto al inventario.

    Parámetros:
        inventario (list): Lista de diccionarios con los productos.
        nombre (str): Nombre del producto.
        precio (float): Precio unitario del producto.
        cantidad (int): Cantidad disponible en inventario.

    Retorno:
        bool: True si se agregó correctamente, False si el producto ya existe.
    """
    # Verificar si el producto ya existe (búsqueda case-insensitive)
    if buscar_producto(inventario, nombre) is not None:
        print(f"  ⚠  El producto '{nombre}' ya existe. Use 'Actualizar' para modificarlo.")
        return False

    inventario.append({
        "nombre": nombre,
        "precio": float(precio),
        "cantidad": int(cantidad)
    })
    print(f"  ✔  Producto '{nombre}' agregado exitosamente.")
    return True


def mostrar_inventario(inventario):
    """
    Imprime todos los productos del inventario en formato tabular.

    Parámetros:
        inventario (list): Lista de diccionarios con los productos.

    Retorno:
        None
    """
    if not inventario:
        print("  ℹ  El inventario está vacío.")
        return

    # Encabezado de tabla
    print("\n" + "=" * 55)
    print(f"  {'#':<4} {'Nombre':<20} {'Precio':>10} {'Cantidad':>10}")
    print("=" * 55)

    for i, producto in enumerate(inventario, start=1):
        print(f"  {i:<4} {producto['nombre']:<20} "
              f"${producto['precio']:>9.2f} {producto['cantidad']:>10}")

    print("=" * 55)
    print(f"  Total de productos: {len(inventario)}\n")


def buscar_producto(inventario, nombre):
    """
    Busca un producto en el inventario por nombre (sin distinguir mayúsculas).

    Parámetros:
        inventario (list): Lista de diccionarios con los productos.
        nombre (str): Nombre del producto a buscar.

    Retorno:
        dict | None: Diccionario del producto si se encuentra, None si no existe.
    """
    nombre_lower = nombre.strip().lower()
    for producto in inventario:
        if producto["nombre"].lower() == nombre_lower:
            return producto
    return None


def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """
    Actualiza el precio y/o la cantidad de un producto existente.

    Parámetros:
        inventario (list): Lista de diccionarios con los productos.
        nombre (str): Nombre del producto a actualizar.
        nuevo_precio (float, opcional): Nuevo precio; None para no cambiar.
        nueva_cantidad (int, opcional): Nueva cantidad; None para no cambiar.

    Retorno:
        bool: True si se actualizó, False si el producto no existe.
    """
    producto = buscar_producto(inventario, nombre)

    if producto is None:
        print(f"  ✖  Producto '{nombre}' no encontrado.")
        return False

    # Aplicar cambios solo si se proporcionaron valores
    if nuevo_precio is not None:
        producto["precio"] = float(nuevo_precio)
    if nueva_cantidad is not None:
        producto["cantidad"] = int(nueva_cantidad)

    print(f"  ✔  Producto '{producto['nombre']}' actualizado: "
          f"precio=${producto['precio']:.2f}, cantidad={producto['cantidad']}.")
    return True


def eliminar_producto(inventario, nombre):
    """
    Elimina un producto del inventario por nombre.

    Parámetros:
        inventario (list): Lista de diccionarios con los productos.
        nombre (str): Nombre del producto a eliminar.

    Retorno:
        bool: True si se eliminó, False si el producto no existe.
    """
    producto = buscar_producto(inventario, nombre)

    if producto is None:
        print(f"  ✖  Producto '{nombre}' no encontrado.")
        return False

    inventario.remove(producto)
    print(f"  ✔  Producto '{nombre}' eliminado del inventario.")
    return True


def calcular_estadisticas(inventario):
    """
    Calcula métricas estadísticas del inventario.

    Parámetros:
        inventario (list): Lista de diccionarios con los productos.

    Retorno:
        dict: Diccionario con las métricas:
              - unidades_totales (int)
              - valor_total (float)
              - producto_mas_caro (dict con 'nombre' y 'precio')
              - producto_mayor_stock (dict con 'nombre' y 'cantidad')
              Retorna None si el inventario está vacío.
    """
    if not inventario:
        print("  ℹ  El inventario está vacío, no hay estadísticas que calcular.")
        return None

    # Lambda para calcular subtotal de cada producto
    subtotal = lambda p: p["precio"] * p["cantidad"]

    unidades_totales = sum(p["cantidad"] for p in inventario)
    valor_total = sum(subtotal(p) for p in inventario)
    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])

    stats = {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": {
            "nombre": producto_mas_caro["nombre"],
            "precio": producto_mas_caro["precio"]
        },
        "producto_mayor_stock": {
            "nombre": producto_mayor_stock["nombre"],
            "cantidad": producto_mayor_stock["cantidad"]
        }
    }

    # Mostrar estadísticas con formato legible
    print("\n" + "=" * 45)
    print("         📊  ESTADÍSTICAS DEL INVENTARIO")
    print("=" * 45)
    print(f"  Unidades totales en stock : {unidades_totales}")
    print(f"  Valor total del inventario: ${valor_total:,.2f}")
    print(f"  Producto más caro         : {producto_mas_caro['nombre']} "
          f"(${producto_mas_caro['precio']:.2f})")
    print(f"  Mayor stock               : {producto_mayor_stock['nombre']} "
          f"({producto_mayor_stock['cantidad']} unidades)")
    print("=" * 45 + "\n")

    return stats
