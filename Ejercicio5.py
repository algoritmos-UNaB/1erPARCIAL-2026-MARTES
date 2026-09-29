def contar_libros(biblioteca):
    total = 0
    for libro in biblioteca.libros:
        total += 1
    return total