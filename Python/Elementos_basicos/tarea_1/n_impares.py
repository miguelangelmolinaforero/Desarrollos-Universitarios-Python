print('Numeros Impares')
a = int(input('Ingrese el número 1: '))
b = int(input('Ingrese el número 2: '))

for a in range(b + 1):
    if a % 2 != 0:
        print(str(a) + ' es impar')