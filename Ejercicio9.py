class TiendaComics:
    def __init__(self):
        self.secciones = {}

    def agregar_comic(self, seccion, comic):
        if seccion not in self.secciones:
            self.secciones[seccion] = []
        self.secciones[seccion].append(comic)

    def remover_comic(self, seccion, comic):
        if seccion in self.secciones and comic in self.secciones[seccion]:
            self.secciones[seccion].remove(comic)

    def actualizar_stock(self, seccion, comic, nuevo_stock):
        if seccion in self.secciones:
            for c in self.secciones[seccion]:
                if c == comic:
                    c.stock = nuevo_stock

    def contar_stock_critico(self):
        contador = 0
        for comics in self.secciones.values():
            for comic in comics:
                if comic.stock <= 3:
                    contador += 1
        return contador

    def retirar_stock_critico(self):
        for seccion in self.secciones.values():
            seccion[:] = [comic for comic in seccion if comic.stock > 3]