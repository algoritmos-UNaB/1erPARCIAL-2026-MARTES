def contar_libros_recursivo(biblioteca, indice=0):
    if indice == len(biblioteca.libros):
        return 0

    return 1 + contar_libros_recursivo(biblioteca, indice + 1)