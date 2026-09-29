from Ejercicio2 import Biblioteca

def cantidad_libros(biblioteca, i=0):
    if i == len(biblioteca.libros):
        return 0
    return 1 + cantidad_libros(biblioteca, i + 1)