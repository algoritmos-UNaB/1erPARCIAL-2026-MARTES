class Nodo:
    def __init__(self, dato, sig=None):
        self._elem = dato
        self._nxt = sig

class ListaEnlazada:
    def __init__(self):
        self.header = None
    
    def __iter__(self):
        self._nodo_actual_iter= self.header
        return self
    def __next__(self):
        if self._nodo_actual_iter is None:
            raise StopIteration 
        elemento_devolver = self._nodo_actual_iter
        self._nodo_actual_iter = self._nodo_actual_iter._next
        return elemento_devolver