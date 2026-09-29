from Ejercicio2 import Biblioteca

def iter_cont_total(biblioteca):
    contador = 0
    for i in biblioteca._libros:
        contador += 1
    return contador