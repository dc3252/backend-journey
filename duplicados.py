#duplicados
original = [4, 2, 4, 7, 2, 9, 7, 1]

sin_duplicados = []

for elemento in original:
    if elemento not in sin_duplicados:
        sin_duplicados.append(elemento)

print(sin_duplicados)