#(1pt.) Ejercicio 5: El Conteo de Libros de Leonard (Iterativo)
#Implementar una función iterativa que calcule la cantidad total 
#de libros en una biblioteca (de la clase Biblioteca definida con anterioridad).
# notas
# Pide un bucle, que vaya recorriendo y contando los objetos de la lista/ biblioteca

def contar_leonard(biblioteca):
    n_libros = 0

    for libro in biblioteca.libros:
        n_libros = n_libros + 1
    return n_libros
    

