from datetime import date
from Ejercicio7 import Comic
from Ejercicio10 import ListaEnlazada

class TiendaComics:
    def __init__(self):
        self.secciones = {}  # nombre de sección -> ListaEnlazada de Comic

    def agregar_comic(self, seccion, comic):
        if seccion not in self.secciones:
            self.secciones[seccion] = ListaEnlazada()
        self.secciones[seccion].agregar_al_final(comic)

    def remover_comic(self, id_comic):
        for lista in self.secciones.values():
            for comic in lista:
                if comic.id_comic == id_comic:
                    lista.eliminar(comic)
                    return

    def actualizar_stock(self, id_comic, nuevo_stock):
        for lista in self.secciones.values():
            for comic in lista:
                if comic.id_comic == id_comic:
                    comic.stock = nuevo_stock
                    return

    def retirar_stock_critico(self):
        cantidad = 0
        for lista in self.secciones.values():
            criticos = []
            for comic in lista:
                if comic.stock <= 3:
                    criticos.append(comic)
            for comic in criticos:
                lista.eliminar(comic)
                cantidad += 1
        return cantidad

if __name__ == "__main__":
    tienda = TiendaComics()
    tienda.agregar_comic("DC Comics", Comic("Batman #1", 1, date(2024, 6, 1), 7.50, 10))
    tienda.agregar_comic("DC Comics", Comic("The Flash #1", 2, date(2024, 5, 10), 5.99, 2))
    tienda.agregar_comic("Marvel", Comic("Spider-Man #1", 3, date(2024, 3, 15), 6.99, 3))

    print(tienda.retirar_stock_critico())  # 2