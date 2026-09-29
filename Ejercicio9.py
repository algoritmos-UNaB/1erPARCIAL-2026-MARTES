#La gestion de la tienda Comics.
class TiendaComics(object):
    def __init__(self):
        self.secciones = {}
    def agregar_comic(self, seccion, comic):
        if not isinstance (comic, Comic):
            raise TypeError ("Se esperaba un objeto Comic.")
        if seccion not in self.secciones:
            self.secciones[seccion] = []
        self.secciones[seccion].append(comic)
    def remover_comic(self, seccion, id_comic):
        if seccion not in self.secciones:
            raise KeyError("La sección no existe.")
        for comic in self.secciones[seccion]:
            if comic.id_comic == id_comic:
                self.secciones[seccion].remove(comic)
                return comic
        raise ValueError ("El comic no está en la sección.")
    def actualizar_stock(self, seccion, id_comic, nuevo_stock)
        if seccion not in self.secciones:
            raise KeyError ("La sección no existe.")
        for comic in self.secciones[seccion]:
            if comic.id_comic == id_comic:
                comic.stock = nuevo_stock
                return
        raise ValueError ("El comic no está en la sección.")
    def contar_stock(self):
        total = 0
        for lista in self.secciones.values():
            for comic in lista:
                total += comic.stock
        return total
    def remover_stock_critico(self):
        removidos = []
        for seccion in self.secciones:
            conservados = []
            for comic in self.secciones[seccion]:
                if comic.stock <= 3:
                    removidos.append(comic)
                else:
                    conservados.append(comic)
            self.secciones[seccion] = conservados
        return removidos  