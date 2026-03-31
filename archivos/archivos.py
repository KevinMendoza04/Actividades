import csv
import os

# Encabezado esperado en el archivo CSV
HEADER_ESPERADO = ["nombre", "precio", "cantidad"]


def guardar_csv(inventario, ruta, incluir_header=True):
    """
    Guarda el inventario en un archivo CSV.

    Parámetros:
        inventario (list): Lista de diccionarios con los productos.
        ruta (str): Ruta del archivo CSV de destino.
        incluir_header (bool): Si True, escribe la fila de encabezado.

    Retorno:
        bool: True si se guardó correctamente, False en caso de error.
    """
    # Validar que el inventario no esté vacío
    if not inventario:
        print("  ⚠  El inventario está vacío. No hay nada que guardar.")
        return False

    try:
        with open(ruta, mode="w", newline="", encoding="utf-8") as archivo:
            writer = csv.DictWriter(archivo, fieldnames=HEADER_ESPERADO)

            if incluir_header:
                writer.writeheader()  # Escribe: nombre,precio,cantidad

            for producto in inventario:
                # Escribir solo los campos relevantes
                writer.writerow({
                    "nombre": producto["nombre"],
                    "precio": producto["precio"],
                    "cantidad": producto["cantidad"]
                })

        print(f"  ✔  Inventario guardado en: {ruta}")
        return True

    except PermissionError:
        print(f" Sin permisos para escribir en '{ruta}'. "
              "Verifique los permisos del archivo/directorio.")
    except OSError as e:
        print(f" Error al escribir el archivo: {e}")
    except Exception as e:
        print(f" Error inesperado al guardar: {e}")

    return False


def cargar_csv(ruta):
    """
    Carga productos desde un archivo CSV con validaciones por fila.

    Parámetros:
        ruta (str): Ruta del archivo CSV a cargar.

    Retorno:
        tuple: (lista_productos, errores)
               - lista_productos (list): productos válidos cargados.
               - errores (int): cantidad de filas inválidas omitidas.
               Retorna (None, 0) si ocurre un error crítico de lectura.
    """
    productos_validos = []
    errores = 0

    try:
        with open(ruta, mode="r", newline="", encoding="utf-8") as archivo:
            reader = csv.reader(archivo)

            # Leer y validar encabezado
            try:
                header = next(reader)
            except StopIteration:
                print(" El archivo está vacío.")
                return None, 0

            # Normalizar encabezado (strip + lowercase)
            header_normalizado = [col.strip().lower() for col in header]
            if header_normalizado != HEADER_ESPERADO:
                print(f" Encabezado inválido: {header}. "
                      f"Se esperaba: {','.join(HEADER_ESPERADO)}")
                return None, 0

            # Procesar cada fila de datos
            for num_fila, fila in enumerate(reader, start=2):  # fila 2 = primera de datos
                # Validar cantidad de columnas
                if len(fila) != 3:
                    print(f" Fila {num_fila} omitida (columnas incorrectas): {fila}")
                    errores += 1
                    continue

                nombre, precio_str, cantidad_str = fila

                # Validar nombre no vacío
                nombre = nombre.strip()
                if not nombre:
                    print(f" Fila {num_fila} omitida (nombre vacío).")
                    errores += 1
                    continue

                # Validar y convertir precio
                try:
                    precio = float(precio_str.strip())
                    if precio < 0:
                        raise ValueError("precio negativo")
                except ValueError:
                    print(f" Fila {num_fila} omitida (precio inválido: '{precio_str}').")
                    errores += 1
                    continue

                # Validar y convertir cantidad
                try:
                    cantidad = int(cantidad_str.strip())
                    if cantidad < 0:
                        raise ValueError("cantidad negativa")
                except ValueError:
                    print(f" Fila {num_fila} omitida (cantidad inválida: '{cantidad_str}').")
                    errores += 1
                    continue

                # Fila válida: agregar al resultado
                productos_validos.append({
                    "nombre": nombre,
                    "precio": precio,
                    "cantidad": cantidad
                })

    except FileNotFoundError:
        print(f"  ✖  Archivo no encontrado: '{ruta}'.")
        return None, 0
    except UnicodeDecodeError:
        print(f"  ✖  Error de codificación al leer '{ruta}'. "
              "Asegúrese de que el archivo esté en formato UTF-8.")
        return None, 0
    except Exception as e:
        print(f"  ✖  Error inesperado al leer el archivo: {e}")
        return None, 0

    return productos_validos, errores


def fusionar_inventario(inventario_actual, productos_nuevos):
    """
    Fusiona productos cargados con el inventario actual.

    Política de fusión:
        - Si el nombre ya existe: se suma la cantidad y se actualiza el precio al nuevo.
        - Si no existe: se agrega como producto nuevo.

    Parámetros:
        inventario_actual (list): Inventario en memoria.
        productos_nuevos (list): Lista de productos a fusionar.

    Retorno:
        tuple: (agregados, actualizados) contadores de cada acción.
    """
    print("\n  Política de fusión: si el producto ya existe, "
          "se SUMA la cantidad y se ACTUALIZA el precio al nuevo valor.")

    agregados = 0
    actualizados = 0

    for nuevo in productos_nuevos:
        # Buscar si ya existe en el inventario actual
        existente = next(
            (p for p in inventario_actual
             if p["nombre"].lower() == nuevo["nombre"].lower()),
            None
        )

        if existente:
            # Actualizar precio y sumar cantidad
            existente["precio"] = nuevo["precio"]
            existente["cantidad"] += nuevo["cantidad"]
            actualizados += 1
        else:
            # Agregar como nuevo
            inventario_actual.append(nuevo)
            agregados += 1

    return agregados, actualizados
