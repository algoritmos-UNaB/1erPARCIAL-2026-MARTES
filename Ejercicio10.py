class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.tamano = 0

    def agregar(self, dato):
        nuevo = Nodo(dato)

        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

        self.tamano += 1

    def remover(self, dato):
        actual = self.cabeza
        anterior = None

        while actual:
            if actual.dato == dato:
                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente

                self.tamano -= 1
                return True

            anterior = actual
            actual = actual.siguiente

        return False

    def __len__(self):
        return self.tamano