class Nodo:
    def __init__(self, dato, sig=None):
        self._elem = dato
        self._nxt = sig


class IteradorListaEnlazada:
    def __init__(self, inicio):
        self.actual = inicio

    def __iter__(self):
        return self

    def __next__(self):
        if self.actual == None:
            raise StopIteration
        dato = self.actual._elem
        self.actual = self.actual._nxt
        return dato


class ListaEnlazada:
    def __init__(self):
        self.header = None
        self._tamano = 0

    def esta_vacia(self):
        if self.header == None:
            return True
        else:
            return False

    def append(self, dato):
        nodo_nuevo = Nodo(dato)
        if self.header == None:
            self.header = nodo_nuevo
        else:
            aux = self.header
            while aux._nxt != None:
                aux = aux._nxt
            aux._nxt = nodo_nuevo
        self._tamano += 1

    def remove(self, dato):
        if self.esta_vacia():
            return

        if self.header._elem == dato:
            self.header = self.header._nxt
            self._tamano -= 1
            return

        anterior = self.header
        actual = self.header._nxt

        while actual != None:
            if actual._elem == dato:
                anterior._nxt = actual._nxt
                self._tamano -= 1
                return
            anterior = actual
            actual = actual._nxt

    def __len__(self):
        return self._tamano

    def __iter__(self):
        return IteradorListaEnlazada(self.header)

    def __str__(self):
        elementos = [str(elem) for elem in self]
        return "[" + ", ".join(elementos) + "]"