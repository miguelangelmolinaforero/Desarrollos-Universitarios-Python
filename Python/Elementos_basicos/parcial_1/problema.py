# Realizar un Script en Python que permita conocer de dos numeros ingresados por el usuario, cual es el mayor

a = int(input('Ingrese el número 1: '))
b = int(input('Ingrese el número 2: '))
print()

if a > b:
    print(str(a) + " es mayor que " + str(b))
elif a < b:
    print(str(b) + " es mayor que " + str(a))
elif a == b:
    print(str(a) + " es igual que " + str(b))