

print("----------MENÚ-----------")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")

respuesta = int(input('Ingresa un número: '))

a = int(input('Ingrese el número 1: '))
b = int(input('Ingrese el número 2: '))
print('OPERACIONES BASICAS')
if respuesta == 1:
    suma = a + b
    print('La suma es: ' + str(suma))
if respuesta == 2:
    resta = a - b
    print('La resta es: ' + str(resta))
if respuesta == 2:
    multiplicacion = a * b
    print('La multiplicacion es: ' + str(multiplicacion))
if respuesta == 2:
    division = a / b
    print('La division es: ' + str(division))

for x in range(121):
    if x % 2 == 0:
        print('par ' + str(x))


def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(1000)

print('Numeros Impares')
a = int(input('Ingrese el número 1: '))
b = int(input('Ingrese el número 2: '))

for a in range(b):
    if a % 2 != 0:
        print(str(a) + ' es impar')
print('listo')

print('PORCENTAJE')

a = int(input('Ingrese el número 1: '))
porcentaje = int(input('Ingrese el porcentaje a calcular: '))
if porcentaje > 100 or porcentaje < 0:
    print("Vuelva a intentarlo")

elif porcentaje <= 100 and porcentaje >= 0:
    total = a * porcentaje / 100
    print('El porcentaje es: ' + str(total))
