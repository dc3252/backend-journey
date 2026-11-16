#promedio
numeros = [8, 3, 15, -4, 7, 22, 10]

if len(numeros) == 0:
    print("La lista está vacía")
else:
    suma = 0
    mayor = numeros[0]
    menor = numeros[0]

    for n in numeros:
        suma = suma + n          

        if n > mayor:            
            mayor = n

        if n < menor:            
            menor = n

    promedio = suma / len(numeros)

    print("Suma:", suma)
    print("Promedio:", promedio)
    print("Máximo:", mayor)
    print("Mínimo:", menor)