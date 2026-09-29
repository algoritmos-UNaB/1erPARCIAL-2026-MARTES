class TiendaComics:
    def __init__(self):
        self.secciones = {
            "DC Comics": [],
            "Marvel": [],
            "Independientes": []
        }

    def agregar_comic(self, seccion, comic):
        if seccion in self.secciones:
            self.secciones[seccion].append(comic)
        else:
            print("Seccion no encontrada en la tienda")

    def remover_comic(self, seccion, comic):
        if seccion in self.secciones:
            if comic in self.secciones[seccion]:
                self.secciones[seccion].remove(comic)
            else:
                pass

    def actualizar_stock(self, seccion, id_comic, nuevo_stock):
        if seccion in self.secciones:
            for c in self.secciones[seccion]:
                if c.id_comic == id_comic:
                    c.stock = nuevo_stock
                    break

    def limpiar_stock_critico(self):
        total_retirados = 0

        for sec, lista_comics in self.secciones.items():
            a_eliminar = []

            for item in lista_comics:
                if item.stock <= 3:
                    total_retirados += 1
                    a_eliminar.append(item)

            for item in a_eliminar:
                lista_comics.remove(item)

        return total_retirados                    
