class Nodo:
    def __init__(self, dato, sig=None):
        self._elem = dato
        self._nxt = sig

class ListaEnlazada:
    def __init__(self):
        self.header = None
        self.size = 0
    
    def is_empty(self):
        if self.header is None:
            return True
        else:
            return False

    def agregar_inicio(self, dato):
        self.header = Nodo(dato, self.header)
        self.size += 1
    
#No se termino este ejercicio