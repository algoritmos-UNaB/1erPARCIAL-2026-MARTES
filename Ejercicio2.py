from Ejercicio10 import ListaEnlazada

class Biblioteca:
    def __init__(self):
        self.libros = ListaEnlazada()

    # punto 2
    def esta_vacia(self):
        return self.libros.esta_vacia()

    def agregar_libro(self, libro):
        self.libros.agregar_al_final(libro)

    def remover_libro(self, libro):
        self.libros.eliminar(libro)

    # punto 3
    def leer_primer_libro(self):
        return self.libros.leer_primero()

    def leer_ultimo_libro(self):
        return self.libros.leer_ultimo()

    def insertar_al_principio(self, libro):
        self.libros.agregar_al_principio(libro)

    def agregar_al_final(self, libro):
        self.libros.agregar_al_final(libro)

    # punto 4
    def __len__(self):
        return len(self.libros)

    def __str__(self):
        return "Biblioteca con " + str(len(self)) + " libros: " + str(self.libros)

    def __eq__(self, otra):
        if len(self) != len(otra):
            return False
        nodo_a = self.libros.header
        nodo_b = otra.libros.header
        while nodo_a is not None:
            if nodo_a._elem != nodo_b._elem:
                return False
            nodo_a = nodo_a._nxt
            nodo_b = nodo_b._nxt
        return True

    def __add__(self, otra):
        nueva = Biblioteca()
        for libro in self.libros:
            nueva.agregar_libro(libro)
        for libro in otra.libros:
            nueva.agregar_libro(libro)
        return nueva

if __name__ == "__main__":
    a = Biblioteca()
    b = Biblioteca()
    a.agregar_libro("Dune")
    a.agregar_libro("1984")
    b.agregar_libro("Dune")
    b.agregar_libro("1984")
    print(a == b)   # True
    b.agregar_libro("Cosmos")
    print(a == b)   # False