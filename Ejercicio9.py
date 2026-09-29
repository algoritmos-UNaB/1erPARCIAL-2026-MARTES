class TiendaComics:
    def __init__(self):
        self.secciones = {}

    def agregar_comic(self, seccion: str, comic):
        if seccion not in self.secciones:
            self.secciones[seccion] = []
        self.secciones[seccion].append(comic)

    def remover_comic(self, comic):
        for lista_comics in self.secciones.values():
            if comic in lista_comics:
                lista_comics.remove(comic)
                return True
        return False

    def actualizar_stock(self, comic, nuevo_stock: int):
        comic.stock = nuevo_stock

    def limpiar_stock_critico(self):
        eliminados = 0
        for seccion in self.secciones:
            sobresalientes = [c for c in self.secciones[seccion] if c.stock > 3]
            eliminados += len(self.secciones[seccion]) - len(sobresalientes)
            self.secciones[seccion] = sobresalientes
        return eliminados