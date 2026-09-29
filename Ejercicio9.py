from Ejercicio8 import Comic

class TiendaComics:
    def __init__(self):
        self.secciones = {}

    def crear_seccion(self, nombre):
        if nombre not in self.secciones:
            self.secciones[nombre] = []

    def agregar_comic(self, nombre_seccion, comic):
        if not isinstance(comic, Comic):
            raise TypeError("Se debe pasar una instancia de Comic.")
        self.crear_seccion(nombre_seccion)
        self.secciones[nombre_seccion].append(comic)

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
        lista.remove(comic)
        return True

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
        for nombre, lista in list(self.secciones.items()):
            no_criticos = []
            for comic in lista:
                if comic.stock <= umbral:
                    removidos += 1
                else:
                    no_criticos.append(comic)
            self.secciones[nombre] = no_criticos
        return removidos

    def obtener_inventario(self):
        return self.secciones

    def buscar_comic(self, id_comic):
        for lista in self.secciones.values():
            comic = self._buscar_por_id(lista, id_comic)
            if comic is not None:
                return comic
        return None
