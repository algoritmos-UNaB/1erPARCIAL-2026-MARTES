def contar_libros_iterativo(biblioteca):
    contador = 0
    for libro in biblioteca.libros:
        contador +=1
    return contador