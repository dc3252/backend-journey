#listas
lista1 = [1, 2, 2, 3, 4, 5, 8]
lista2 = [4, 5, 5, 6, 7, 8, 9]

comunes = set(lista1) & set(lista2)

print("Como set:", comunes)
print("Como lista:", list(comunes))
print("Ordenada:", sorted(comunes))