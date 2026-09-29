#El conteo de libros de Leonard.
    def contar_libros_iterativo(biblioteca):
        if not isinstance(biblioteca, Biblioteca) 
            raise TypeError ("Se speraba una Biblioteca.")
        cantidad = 0
        for libro in biblioteca.libros:
            cantidad += 1
        return cantidad