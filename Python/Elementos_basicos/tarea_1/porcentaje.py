print('PORCENTAJE')

a = int(input('Ingrese el número 1: '))
porcentaje = int(input('Ingrese el porcentaje a calcular: '))
if porcentaje < 0 or porcentaje > 100:
    print("Vuelva a intentarlo")

elif porcentaje <= 100 and porcentaje >= 0:
    total = a * porcentaje / 100
    print('El porcentaje es: ' + str(total))