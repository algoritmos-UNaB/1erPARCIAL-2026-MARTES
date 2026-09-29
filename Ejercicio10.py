from Ejercicio8 import Comic


# ---------- 10.1 y 10.2: Lista enlazada e iterador ----------

class Nodo:
    def __init__(self, dato, sig=None):
        self._elem = dato
        self._nxt = sig


class IteradorListaEnlazada:
    def __init__(self, nodo_inicial):
        self._actual = nodo_inicial

    def __iter__(self):
        return self

    def __next__(self):
        if self._actual is None:
            raise StopIteration
        elem = self._actual._elem
        self._actual = self._actual._nxt
        return elem


class ListaEnlazada:
    def __init__(self):
        self.header = None
        self._tam = 0

    def esta_vacia(self):
        return self.header is None

    def __len__(self):
        return self._tam

    def primero(self):
        if self.esta_vacia():
            return None
        return self.header._elem

    def ultimo(self):
        if self.esta_vacia():
            return None
        actual = self.header
        while actual._nxt is not None:
            actual = actual._nxt
        return actual._elem

    def __getitem__(self, indice):
        if indice < 0:
            indice += self._tam
        if indice < 0 or indice >= self._tam:
            raise IndexError("índice fuera de rango")
        actual = self.header
        for _ in range(indice):
            actual = actual._nxt
        return actual._elem

    def __contains__(self, elem):
        for x in self:
            if x == elem:
                return True
        return False

    def agregar_al_principio(self, elem):
        self.header = Nodo(elem, self.header)
        self._tam += 1

    def agregar_al_final(self, elem):
        nuevo = Nodo(elem)
        if self.header is None:
            self.header = nuevo
        else:
            actual = self.header
            while actual._nxt is not None:
                actual = actual._nxt
            actual._nxt = nuevo
        self._tam += 1

    def extender(self, iterable):
        cola = None
        if self.header is not None:
            cola = self.header
            while cola._nxt is not None:
                cola = cola._nxt
        for elem in iterable:
            nuevo = Nodo(elem)
            if cola is None:
                self.header = nuevo
            else:
                cola._nxt = nuevo
            cola = nuevo
            self._tam += 1

    def remover(self, elem):
        previo = None
        actual = self.header
        while actual is not None:
            if actual._elem == elem:
                if previo is None:
                    self.header = actual._nxt
                else:
                    previo._nxt = actual._nxt
                self._tam -= 1
                return True
            previo = actual
            actual = actual._nxt
        return False

    def __iter__(self):
        return IteradorListaEnlazada(self.header)

    def __eq__(self, otra):
        if not isinstance(otra, ListaEnlazada):
            return NotImplemented
        if len(self) != len(otra):
            return False
        for a, b in zip(self, otra):
            if a != b:
                return False
        return True

    def __str__(self):
        return "[" + ", ".join(str(x) for x in self) + "]"


# ---------- 10.1: Biblioteca con lista enlazada ----------

class Biblioteca:

    def __init__(self):
        self._libros = ListaEnlazada()

    def esta_vacia(self):
        return self._libros.esta_vacia()

    def agregar_al_final(self, libro):
        self._libros.agregar_al_final(libro)

    def insertar_al_principio(self, libro):
        self._libros.agregar_al_principio(libro)

    def leer_primer_libro(self):
        return self._libros.primero()

    def leer_ultimo_libro(self):
        return self._libros.ultimo()

    def remover_libro(self, libro):
        if not self._libros.remover(libro):
            print(f'"{libro}" no está en la biblioteca.')

    def cantidad_libros(self):
        return len(self._libros)

    def __len__(self):
        return len(self._libros)

    def __iter__(self):
        return iter(self._libros)

    def __str__(self):
        if self.esta_vacia():
            return "Biblioteca vacia."
        return "Biblioteca: " + ", ".join(self._libros)

    def __eq__(self, otra):
        if not isinstance(otra, Biblioteca):
            return False
        return self._libros == otra._libros

    def __add__(self, otra):
        if not isinstance(otra, Biblioteca):
            return NotImplemented
        nueva = Biblioteca()
        nueva._libros.extender(self._libros)
        nueva._libros.extender(otra._libros)
        return nueva


# ---------- 10.1: TiendaComics con lista enlazada ----------

class TiendaComics:
    def __init__(self):
        self.secciones = {}

    def crear_seccion(self, nombre):
        if nombre not in self.secciones:
            self.secciones[nombre] = ListaEnlazada()

    def agregar_comic(self, nombre_seccion, comic):
        if not isinstance(comic, Comic):
            raise TypeError("Se debe pasar una instancia de Comic.")
        self.crear_seccion(nombre_seccion)
        self.secciones[nombre_seccion].agregar_al_final(comic)

    def _buscar_por_id(self, lista, id_comic):
        for c in lista:
            if c.id_comic == id_comic:
                return c
        return None

    def remover_comic(self, nombre_seccion, id_comic):
        if nombre_seccion not in self.secciones:
            return False
        lista = self.secciones[nombre_seccion]
        comic = self._buscar_por_id(lista, id_comic)
        if comic is None:
            return False
        return lista.remover(comic)

    def actualizar_stock(self, nombre_seccion, id_comic, nuevo_stock):
        if nombre_seccion not in self.secciones:
            return False
        comic = self._buscar_por_id(self.secciones[nombre_seccion], id_comic)
        if comic is None:
            return False
        comic.stock = int(nuevo_stock)
        return True

    def contar_criticos_y_remover(self, umbral=3):
        removidos = 0
        for lista in self.secciones.values():
            criticos = [c for c in lista if c.stock <= umbral]
            for c in criticos:
                lista.remover(c)
                removidos += 1
        return removidos

    def obtener_inventario(self):
        return self.secciones

    def buscar_comic(self, id_comic):
        for lista in self.secciones.values():
            comic = self._buscar_por_id(lista, id_comic)
            if comic is not None:
                return comic
        return None