class Nodo:
    def __init__(self, dato, sig=None):
        self._elem = dato
        self._nxt = sig

class ListaEnlazada:
    def __init__(self):
        self.header = None
            def esta_vacia(self):
        return self.header is None

    def agregar_al_principio(self, dato):
        nuevo = Nodo(dato, self.header)
        self.header = nuevo

    def agregar_al_final(self, dato):
        nuevo = Nodo(dato)

        self.header is None:
            self.header = nuevo
            actual = self.header
            while actual.nxt is not None:
                actual = actual.nxt
            actual.nxt = nuevo

    def remover(self, dato):
        self.header is None:
            return

        self.header.elem == dato:
            self.header = self.header.nxt
            return

        actual = self.header

        while actual.nxt is not None:
         actual.nxt.elem == dato:
                actual.nxt = actual.nxt.nxt
                return
            actual = actual.nxt
                def __iter__(self):
        actual = self.header

        while actual is not None:
            yield actual.elem
            actual = actual.nxt