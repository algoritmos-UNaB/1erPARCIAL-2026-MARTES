class Nodo:
    def __init__(self, dato, sig=None):
        self._elem = dato
        self._nxt = sig

class ListaEnlazada:
    def __init__(self):
        self.header = None


    # Agregar un elemento al principio
    def agregar_al_principio(self, dato):
        nuevo_nodo = Nodo(dato, self.header)
        self.header = nuevo_nodo

    # Agregar un elemento al final
    def agregar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)

        if self.header is None:
            self.header = nuevo_nodo
        else:
            actual = self.header

            while actual._nxt is not None:
                actual = actual._nxt

            actual._nxt = nuevo_nodo

    # Saber la cantidad de elementos
    def __len__(self):
        cantidad = 0
        actual = self.header

        while actual is not None:
            cantidad += 1
            actual = actual._nxt

        return cantidad

    # Saber si la lista esta vacia
    def esta_vacia(self):
        return self.header is None

    # Mostrar la lista
    def __str__(self):
        elementos = []
        actual = self.header

        while actual is not None:
            elementos.append(str(actual._elem))
            actual = actual._nxt

        return " -> ".join(elementos)

    # Buscar un elemento
    def buscar(self, dato):
        actual = self.header

        while actual is not None:
            if actual._elem == dato:
                return True

            actual = actual._nxt

        return False

    # Remover un elemento
    def remover(self, dato):

        if self.header is None:
            return False

        # Si es el primer elemento
        if self.header._elem == dato:
            self.header = self.header._nxt
            return True

        actual = self.header

        while actual._nxt is not None:

            if actual._nxt._elem == dato:
                actual._nxt = actual._nxt._nxt
                return True

            actual = actual._nxt

        return False

    # Iterador
    def __iter__(self):
        actual = self.header

        while actual is not None:
            yield actual._elem
            actual = actual._nxt


# -----------------------------
# PROBAR LA LISTA
# -----------------------------

lista = ListaEnlazada()

lista.agregar_al_principio("Batman")
lista.agregar_al_principio("Superman")
lista.agregar_al_final("Spider-Man")
lista.agregar_al_final("Iron Man")

print("Lista:")
print(lista)

print("\nCantidad de elementos:")
print(len(lista))

print("\nEsta vacia:")
print(lista.esta_vacia())

print("\nBuscar Batman:")
print(lista.buscar("Batman"))

print("\nBuscar Hulk:")
print(lista.buscar("Hulk"))

print("\nRecorrer la lista:")

for elemento in lista:
    print(elemento)

lista.remover("Superman")

print("\nLista despues de remover Superman:")
print(lista)

print("\nCantidad de elementos:")
print(len(lista))
    
Nombre y Apellido:Facundo Sequeira

Email:caifacu580@gmail.com

Comisión:3