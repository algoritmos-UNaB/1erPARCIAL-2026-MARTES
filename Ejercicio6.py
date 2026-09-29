def contar_libros_recursivo(biblioteca):
    def _contar(lista):
        if not lista:
            return 0
        return 1 + _contar(lista[1:])
    return _contar(biblioteca.libros)