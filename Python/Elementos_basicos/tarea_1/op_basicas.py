print("----------MENÚ-----------")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")
print("5. Todas las opciones")
print()

respuesta = int(input('Ingresa la opción que deseas: '))
print()

a = int(input('Ingrese el número 1: '))
b = int(input('Ingrese el número 2: '))
print()

print('OPERACIONES BASICAS')
print()

if respuesta == 1:
    suma = a + b
    print('La suma es: ' + str(suma))
elif respuesta == 2:
    resta = a - b
    print('La resta es: ' + str(resta))
elif respuesta == 3:
    multiplicacion = a * b
    print('La multiplicacion es: ' + str(multiplicacion))
elif respuesta == 4:
    division = a / b
    print('La division es: ' + str(division))
elif respuesta == 5:
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    print('La suma es: ' + str(suma))
    print('La resta es: ' + str(resta))
    print('La multiplicacion es: ' + str(multiplicacion))
    print('La division es: ' + str(division))
print()
