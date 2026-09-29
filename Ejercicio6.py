def contar_libros_recursivo(biblioteca):
    def contar(lista, indice):
        if indice == len(lista):
            return 0
        return 1 + contar(lista, indice + 1)

    return contar(biblioteca.libros, 0)