import random
Pasajeros = list()
for i in range(24):
    D=random.randint(1,54)
    Pasajeros.append(D)

print(Pasajeros) #Imprime todo la lista

for pasajero in Pasajeros: #Imprime cada elemento de la lista
    print(pasajero)