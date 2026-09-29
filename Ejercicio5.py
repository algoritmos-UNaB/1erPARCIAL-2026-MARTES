def contar_libros_iterativo(biblioteca):
    contador = 0
    # Recorremos cada libro dentro de la lista de la biblioteca
    for libro in biblioteca.libros:
        contador += 1
    return contador
#Itera por la lista de libros (biblioteca.libros) elemento por elemento.