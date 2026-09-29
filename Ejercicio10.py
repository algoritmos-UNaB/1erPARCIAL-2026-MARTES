class Nodo:
    def __init__(self, dato, sig=None):
        self._elem = dato
        self._nxt = sig


class IteradorLista:
    def __init__(self, header):
        self.actual = header

    def __iter__(self):
        return self

    def __next__(self):
        if self.actual is None:
            raise StopIteration
        dato = self.actual._elem
        self.actual = self.actual._nxt
        return dato


class ListaEnlazada:
    def __init__(self):
        self.header = None

    def esta_vacia(self):
        return self.header is None

    def agregar_al_principio(self, dato):
        self.header = Nodo(dato, self.header)

    def agregar_al_final(self, dato):
        nuevo = Nodo(dato)
        if self.header is None:
            self.header = nuevo
        else:
            actual = self.header
            while actual._nxt is not None:
                actual = actual._nxt
            actual._nxt = nuevo

    def eliminar(self, dato):
        anterior = None
        actual = self.header
        while actual is not None:
            if actual._elem == dato:
                if anterior is None:
                    self.header = actual._nxt
                else:
                    anterior._nxt = actual._nxt
                return True
            anterior = actual
            actual = actual._nxt
        return False

    def leer_primero(self):
        if self.header is None:
            return None
        return self.header._elem

    def leer_ultimo(self):
        if self.header is None:
            return None
        actual = self.header
        while actual._nxt is not None:
            actual = actual._nxt
        return actual._elem

    def __len__(self):
        cantidad = 0
        actual = self.header
        while actual is not None:
            cantidad += 1
            actual = actual._nxt
        return cantidad

    def __iter__(self):
        return IteradorLista(self.header)

    def __str__(self):
        elementos = []
        for dato in self:
            elementos.append(str(dato))
        return "[" + ", ".join(elementos) + "]"