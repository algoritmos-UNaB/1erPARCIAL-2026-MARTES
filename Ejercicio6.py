def contar_librosR(Biblioteca,i=0):
    if i==len(Biblioteca.libros):
        return 0
    return 1+contar_librosR(Biblioteca,i+1)