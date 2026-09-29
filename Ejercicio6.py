from Ejercicio2 import Biblioteca

def rec_cont_total(biblioteca, libros=None):
    # Llamada para tomar la lista de la biblioteca
    if libros is None:
        libros = list(biblioteca._libros)
    # Caso Base
    if len(libros == 0):
        return 0
    # Funcion Recursiva
    libros.pop()
    return 1 + rec_cont_total(biblioteca, libros)