def contar_libros_iterativo(biblioteca):
    cantidad = 0

    for libro in biblioteca.libros:
        cantidad += 1

    return cantidad