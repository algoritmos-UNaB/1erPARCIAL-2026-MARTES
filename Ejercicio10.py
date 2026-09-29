class Nodo:
    def __init__(self, dato, sig=None):
        self._elem = dato
        self._nxt = sig

class ListaEnlazada:
    def __init__(self):
        self.header = None
        self._actual= None
    
    def append(self, dato):
        #Insertar nodo al final
        if not self.header:
            self.header = Nodo(dato)
            return
        act = self.header
        while act._nxt:
            act = act._nxt
        act._nxt = Nodo(dato)

    def remove(self, dato):
        if not self.header:
            return False
        if self.header._elem == dato:
            self.header = self.header._nxt
            return True
        act = self.header
        while act._nxt and act._nxt._elem != dato:
            act = act._nxt
        if act._nxt:
            act._nxt = act._nxt._nxt
            return True
        return False

    def __iter__(self):
        self._actual = self.header
        return self

    def __next__(self):
        if not self._actual:
            raise StopIteration
        dato = self._actual._elem
        self._actual = self._actual._nxt
        return dato