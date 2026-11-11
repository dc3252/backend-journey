#cuenta el numero de vocales en un texto
texto = input ("texto ")
vocal ="aeiou"
contar = 0
for w in texto:
    if w in vocal:
        contar +=1
print ("numero de vocales es ", contar)