num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
if num1 == num2:
    print ("The numbers are the same.")
else:
    print ("The numbers are different.")
if num2 > num1:
    print (f"{num1} is shorter than {num2}.")
else:
    print (f"{num1} is bigger than {num2}.")