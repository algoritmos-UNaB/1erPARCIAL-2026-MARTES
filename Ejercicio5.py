def cantidad_libros(biblioteca):
    cantidad = 0

    for libro in biblioteca.libros:
        cantidad += 1

    return cantidad