#Nombre y apellido: Leandro Leonel Veliz
#Email: leandro.leonel.veliz@gmail.com
#Comisión: 3

def contar_libros_iterativo(biblioteca):
    contador = 0
    # Iteramos sobre la lista de libros interna de la clase Biblioteca
    for libro in biblioteca.libros:
        contador += 1
    return contador