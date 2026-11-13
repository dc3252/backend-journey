#cuenta palabras en un texto 
def contar_palabras(texto):
    frecuencias = {}
    for palabra in texto.split():
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return frecuencias

texto = "a ver si esto funciona a a a a"
print(contar_palabras(texto))