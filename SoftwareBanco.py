nombre = input("Nombre de usuario: ")
contraseña = input("Contraseña: ")
saldo = 0
op = ""
while op != "3":
    print(f"Bienvenido {nombre}, que deseas hacer hoy?")
    print ("1. Depositar saldo")
    print ("2. Transferir saldo")
    print ("3. Salir.")
    op = input("Elige una opcion: ")
    if op == "1":
        entrada = (input("Saldo a depositar: ").replace(",", "."))
        try:
            deposito = float(entrada)
            saldo += deposito
            print(f"Nuevo saldo: {saldo}")
        except ValueError:
            print("Entrada invalida. No se modifico el saldo.")
    elif op == "2":
         entrada = (input("Saldo a transferir: ").replace(",", "."))
    try:
            transferencia = float(entrada)
            if transferencia <= saldo:
                saldo -= transferencia
                print(f"Nuevo saldo: {saldo}")
            else:
                print("Fondos insuficientes")
    except ValueError:
            print("Entrada invalida. No se modifico el saldo.")
    elif op == "3":
    print ("Sesion Cerrada.")
    else:
    print("Opcion invalida.")