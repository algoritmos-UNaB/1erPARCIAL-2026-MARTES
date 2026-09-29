from Ejercicio2 import Biblioteca

def contar_libros_iterativo(biblioteca: Biblioteca) -> int:
    """
    Función iterativa que calcula la cantidad total de libros en una biblioteca.
    Recorre elemento por elemento la lista interna de libros.
    """
    contador = 0

    for libro in biblioteca.libros:
        contador += 1
    return contador



if __name__ == "__main__":
    # Creamos una instancia de Biblioteca y agregamos algunos libros
    mi_biblio = Biblioteca("Biblioteca Central UNAB")
    mi_biblio.agregar_al_final("Cien años de soledad")
    mi_biblio.agregar_al_final("El Aleph")
    mi_biblio.agregar_al_final("Rayuela")
    mi_biblio.agregar_al_final("Ficciones")


    total = contar_libros_iterativo(mi_biblio)

    print(f"La cantidad total de libros (calculada de forma iterativa) es: {total}")
