class IteradorLista:
    def __init__(self, cabeza):
        self.actual = cabeza

    def __iter__(self):
        return self

    def __next__(self):
        if self.actual is None:
            raise StopIteration

        dato = self.actual.dato
        self.actual = self.actual.siguiente
        return dato


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.tamano = 0

    def __iter__(self):
        return IteradorLista(self.cabeza)