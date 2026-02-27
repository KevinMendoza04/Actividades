intento = int(input("Avidina el número secreto: "))
secreto = 14
while intento != secreto: 
    print("Incorrecto, sigue adivinando")
    intento = int(input("Adivina el número secreto: "))
print("Correcto!")