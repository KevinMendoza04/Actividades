nombre = input("Nombre de usuario: ")
contraseña = input("Contraseña: ")
saldo1 = 0
saldo2 = 0
op = ""
cuenta1 = ""
cuenta2 = ""
while op != "3":
    print(f"Bienvenido {nombre}, que deseas hacer hoy?")
    print ("1. Depositar saldo")
    print ("2. Transferir saldo")
    print ("3. Consultar saldo.")
    print("4. Salir.")
    op = input("Elige una opcion: ")
    if op == "1":
        entrada = input("Saldo a depositar: ").replace(",", ".")
        try:
            deposito = float(entrada)
            saldo += deposito
            print(f"Nuevo saldo: {saldo}")
        except ValueError:
            print("Entrada invalida. No se modifico el saldo.")
    elif op == "2":
        entrada = input("Saldo a transferir: ").replace(",", ".")
        try:
            transferencia = float(entrada)
            if transferencia <= saldo:
                saldo -= transferencia
                print(f"Nuevo saldo: {saldo}")
            else:
                print("Fondos insuficientes")
        except ValueError:
            print("Entrada invalida. No se modifico el saldo.")
    elif op == "4":
            print ("Sesion Cerrada.")
    elif op == "3":
            print(F"Desea consultar su cuenta de ahorros, o corriente?")
            print(f"1. Ahoros.")
            print(f"2. Corriente.")
            entrada = input("Escoga que cuenta quiere consultar: ").replace(",", ".")
    try:
        cuenta = float(entrada)
        if cuenta == 1:
            print(f"El saldo de su cuenta de ahorros es de: ${saldo1}.")
        else:
            print(f"El saldo de su cuenta corriente es de: ${saldo2}.")
    except ValueError:
            print("Entrada invalida. Intente de nuevo.")
else:
    print("Opcion invalida.")