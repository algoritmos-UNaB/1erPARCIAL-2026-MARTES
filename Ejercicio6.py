def recursivo_libros(biblioteca, lista_pendientes=None):
    if lista_pendientes is None:
        lista_pendientes = biblioteca.libros
            
    if not lista_pendientes:
        return 0
            
    else:
        return 1 + recursivo_libros(biblioteca, lista_pendientes[1:])