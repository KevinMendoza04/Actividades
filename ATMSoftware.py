nombre = input("Nombre de usuario: ")
contraseña = input("Contraseña: ")

saldo1 = 0.0   # Cuenta de ahorros
saldo2 = 0.0   # Cuenta corriente

while True:

    print(f"\nBienvenido {nombre}")
    print("1. Depositar saldo")
    print("2. Transferir saldo")
    print("3. Consultar saldo")
    print("4. Salir")

    op = input("Elige una opcion: ")

    # =======================
    # DEPOSITAR
    # =======================
    if op == "1":

        print("1. Cuenta Ahorros")
        print("2. Cuenta Corriente")

        cuenta = input("¿En qué cuenta deseas depositar?: ")

        entrada = input("Saldo a depositar: ").replace(",", ".")

        try:
            deposito = float(entrada)

            if deposito <= 0:
                print("Monto inválido.")
                continue

            if cuenta == "1":
                saldo1 += deposito
                print(f"Nuevo saldo Ahorros: ${saldo1:.2f}")

            elif cuenta == "2":
                saldo2 += deposito
                print(f"Nuevo saldo Corriente: ${saldo2:.2f}")

            else:
                print("Cuenta inválida.")

        except ValueError:
            print("Entrada inválida.")

    # =======================
    # TRANSFERENCIA
    # =======================
    elif op == "2":

        print("Transferir DESDE:")
        print("1. Ahorros")
        print("2. Corriente")

        origen = input("Selecciona cuenta origen: ")

        entrada = input("Saldo a transferir: ").replace(",", ".")

        try:
            transferencia = float(entrada)

            if transferencia <= 0:
                print("Monto inválido.")
                continue

            comision = transferencia * 0.004  # 4x1000

            # -------- desde AHORROS --------
            if origen == "1":

                if saldo1 >= transferencia:

                    saldo1 -= transferencia
                    saldo2 += transferencia

                    # pagar comisión
                    if saldo1 >= comision:
                        saldo1 -= comision
                    elif saldo2 >= comision:
                        saldo2 -= comision
                    else:
                        print("No hay saldo suficiente para pagar la comisión.")
                        saldo1 += transferencia
                        saldo2 -= transferencia
                        continue

                    print("Transferencia exitosa.")
                    print(f"Comisión 4x1000: ${comision:.2f}")

                else:
                    print("Fondos insuficientes para la transferencia.")

            # -------- desde CORRIENTE --------
            elif origen == "2":

                if saldo2 >= transferencia:

                    saldo2 -= transferencia
                    saldo1 += transferencia

                    # pagar comisión
                    if saldo2 >= comision:
                        saldo2 -= comision
                    elif saldo1 >= comision:
                        saldo1 -= comision
                    else:
                        print("No hay saldo suficiente para pagar la comisión.")
                        saldo2 += transferencia
                        saldo1 -= transferencia
                        continue

                    print("Transferencia exitosa.")
                    print(f"Comisión 4x1000: ${comision:.2f}")

                else:
                    print("Fondos insuficientes para la transferencia.")

            else:
                print("Cuenta inválida.")

        except ValueError:
            print("Entrada inválida.")

    # =======================
    # CONSULTAR SALDO
    # =======================
    elif op == "3":

        print("\n--- SALDOS ---")
        print(f"Cuenta Ahorros: ${saldo1:.2f}")
        print(f"Cuenta Corriente: ${saldo2:.2f}")

    # =======================
    # SALIR
    # =======================
    elif op == "4":
        print("Sesión cerrada.")
        break

    else:
        print("Opción inválida.")