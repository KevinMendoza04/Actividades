total = 0
numero = int(input("Enter a number (0 to stop): "))
while numero != 0:
    total += numero
    numero = int(input("Enter a number (0 to stop): "))
print("Total sum:", total)