from Ejercicio2 import Biblioteca

def cantidad_de_libros (biblioteca):
        cantidad = 0
        
        for libro in biblioteca.libros:
            cantidad += 1
        
        return cantidad
