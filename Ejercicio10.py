class Nodo:
    def __init__(self, dato, sig=None):
        self._elem = dato
        self._nxt = sig

class ListaEnlazada:
    def __init__(self):
        self.header = None
    
    def esta_vacia(self):
        return self.header is None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.header = nuevo_nodo
        else:
            actual = self.header
            while actual._nxt:
                actual = actual._nxt
            actual._nxt = nuevo_nodo

    # 10.2
    
    def __iter__(self):
        return IteradorListaEnlazada(self.header)


class IteradorListaEnlazada:
    def __init__(self, inicio):
        self.actual = inicio

    def __iter__(self):
        return self

    def __next__(self):
        if self.actual is None:
            raise StopIteration
        dato = self.actual._elem
        self.actual = self.actual._nxt
        return dato