#aprobados 
alumnos = [
    {"nombre": "Ana", "nota": 8},
    {"nombre": "Luis", "nota": 5},
    {"nombre": "Marta", "nota": 9},
    {"nombre": "Pedro", "nota": 6},
    {"nombre": "Sofía", "nota": 4},
]

NOTA_MINIMA = 6

aprobados = []
for alumno in alumnos:
    if alumno["nota"] >= NOTA_MINIMA:
        aprobados.append(alumno)

if len(aprobados) == 0:
    print("No hay alumnos aprobados")
else:
    suma = 0
    for alumno in aprobados:
        suma += alumno["nota"]

    promedio = suma / len(aprobados)

    print("Aprobados:")
    for alumno in aprobados:
        print("-", alumno["nombre"], alumno["nota"])

    print("Promedio de aprobados:", round(promedio, 2))