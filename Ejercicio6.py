def conteo_libros_penny(biblioteca, n=None):
    if n is None:
        n = len(biblioteca.libros)

    if n == 0:
        return 0

    return 1 + conteo_libros_penny(biblioteca, n - 1)        