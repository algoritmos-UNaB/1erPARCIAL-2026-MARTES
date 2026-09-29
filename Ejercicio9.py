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
        if seccion in self.secciones and comic in self.secciones[seccion]:
            comic.stock = nuevo_stock

    def stock_critico(self):
        cantidad = 0

        for seccion in self.secciones:
            comics_a_remover = []

            for comic in self.secciones[seccion]:
                if comic.stock <= 3:
                    cantidad += 1
                    comics_a_remover.append(comic)

            for comic in comics_a_remover:
                self.secciones[seccion].remove(comic)

        return cantidad