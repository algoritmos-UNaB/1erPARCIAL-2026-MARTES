#(1pt.) Ejercicio 6: El Conteo de Libros de Penny (Recursivo)
#en una biblioteca (de la clase Biblioteca definida con anterioridad).
# en vez de usar un contador, es con recursividad.

def penny_recursivo(biblioteca, inicio = 0):
    if inicio == len(biblioteca.libros):
        return 0

    return 1 + penny_recursivo(biblioteca, inicio +1)
