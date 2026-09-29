def contar_libros_leonard(biblioteca):
    cantidad = 0
    for _ in biblioteca.libros:
        cantidad += 1
    return cantidad 
