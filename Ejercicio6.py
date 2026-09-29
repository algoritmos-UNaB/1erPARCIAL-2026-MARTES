#El conteo de libros de Penny.
    def contar_libros_recursivo(biblioteca, i=0):
        if not isinstance (biblioteca, Biblioteca):
            raise TypeError ("Se esperaba una bibliooteca.")
        if i >= biblioteca.libros.__len__():
            return 0 
        return 1 + contar_libros_recursivo(biblioteca, i + 1)