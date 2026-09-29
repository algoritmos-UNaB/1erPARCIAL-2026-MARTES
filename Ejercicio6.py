def cantidad_libros_recursiva(biblioteca):
    if biblioteca.esta_vacia():
        return 0
    else:
        ultimo = biblioteca.leer_ultimo_libro()
        biblioteca.remover_libro(ultimo)
        cantidad = 1 + cantidad_libros_recursiva(biblioteca)
        biblioteca.agregar_al_final(ultimo)
        return cantidad