def contar_libros_recursivo(libros):
    #lista está vacía, hay 0 libros
    if not libros:
        return 0
    
    #recursivo: 1 libro actual + contar el resto de la lista
    return 1 + contar_libros_recursivo(libros[1:])