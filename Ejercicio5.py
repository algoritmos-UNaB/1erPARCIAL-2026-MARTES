def contar_libros(biblioteca):

    contador = 0
    
    for l in biblioteca.libros:
        contador += 1
        
    return contador