from Ejercicio2 import Biblioteca

def contar_libros_recursivo(libros: list) -> int:

    if not libros:
        return 0
    return 1 + contar_libros_recursivo(libros[1:])


def obtener_total_libros(biblioteca: Biblioteca) -> int:

    return contar_libros_recursivo(biblioteca.libros)



if __name__ == "__main__":
  
    mi_biblio = Biblioteca("Biblioteca UNAB - Recursión")
    mi_biblio.agregar_al_final("Cien años de soledad")
    mi_biblio.agregar_al_final("El Aleph")
    mi_biblio.agregar_al_final("Rayuela")
    mi_biblio.agregar_al_final("Ficciones")
    mi_biblio.agregar_al_final("Fundación")


    total = obtener_total_libros(mi_biblio)

    print(f"La cantidad total de libros (calculada de forma recursiva) es: {total}")
