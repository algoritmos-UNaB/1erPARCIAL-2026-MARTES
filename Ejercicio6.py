from Ejercicio2 import Biblioteca

def contar_libros_rec(biblioteca):
    return contar(biblioteca.libros.header)

def contar(nodo):
    if nodo is None:
        return 0
    return 1 + contar(nodo._nxt)

if __name__ == "__main__":
    b = Biblioteca()
    b.agregar_libro("Cosmos")
    b.agregar_libro("Dune")
    b.agregar_libro("1984")
    print(contar_libros_rec(b))  