class Nodo:
    def __init__(self, dato, sig=None):
        self._elem = dato  
        self._nxt = sig    

class ListaEnlazada:
    def __init__(self):
        self.header = None 

    def agregar(self, dato):
        """Método auxiliar para añadir elementos al final de la lista."""
        nuevo_nodo = Nodo(dato)
        if self.header is None:
            self.header = nuevo_nodo
        else:
            actual = self.header
            while actual._nxt is not None:
                actual = actual._nxt
            actual._nxt = nuevo_nodo

    def __iter__(self):
        """Cumple con el punto 10.2 devolviendo el iterador personalizado."""
        return IteradorLista(self.header)


# 10.2 Implementar Iteradores para las listas enlazadas
class IteradorLista:
    def __init__(self, nodo_inicial):
        # El iterador guarda el estado actual del recorrido
        self._actual = nodo_inicial

    def __iter__(self):
        return self

    def __next__(self):
        # Si llegamos al final (None), detenemos la iteración
        if self._actual is None:
            raise StopIteration
        
        # Guardamos el dato actual, avanzamos al siguiente nodo, y retornamos el dato
        dato = self._actual._elem
        self._actual = self._actual._nxt
        return dato

#Nombre y apellido: Leandro Leonel Veliz
#Email: leandro.leonel.veliz@gmail.com
#Comisión: 3
        