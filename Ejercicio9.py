from datetime import date

class Comic:
    def __init__(self, titulo, id_comic, fecha_publicacion, precio, stock):
        self.titulo = titulo
        self.id_comic = id_comic
        self.fecha_publicacion = fecha_publicacion
        self.precio = precio
        self.stock = stock

    def modificar_datos(self, titulo=None, precio=None, stock=None):
        if titulo is not None:
            self.titulo = titulo

        if precio is not None:
            self.precio = precio

        if stock is not None:
            self.stock = stock

    def calcular_dias(self, fecha_referencia):
        diferencia = (self.fecha_publicacion - fecha_referencia).days

        if diferencia < 0:
            print("El comic es más antiguo que la fecha de referencia.")
            self.stock = 0
        return abs(diferencia)

    def __str__(self):
        return (f"Comic: {self.titulo} | "
                f"ID: {self.id_comic} | "
                f"Precio: ${self.precio} | "
                f"Stock: {self.stock}")

    def __eq__(self, otro):
        return self.id_comic == otro.id_comic and self.titulo == otro.titulo


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

    def remover_comic(self, seccion, comic):
        if seccion in self.secciones and comic in self.secciones[seccion]:
      aaccion].remove(comic)

    
    def actualizar_stock(self, id_comic, nuevo_stock):
        for lista in self.secciones.values():
            for comic in lista:
                if comic.id_comic == id_comic:
                    comic.stock = nuevo_stock
                    return

    def eliminar_stock_critico(self):
        cantidad = 0

        for seccion in self.secciones:
            sobrevivientes = []

            for comic in self.secciones[seccion]:
                if comic.stock <= 3:
                    cantidad += 1
               sobrevivientes.append(comic)

            self.secciones[seccion] = sobrevivientes

        return cantidad

    def mostrar_inventario(self):
        for seccion, comics in self.secciones.items():
            print(f"\n{seccion}:")
            for comic in comics:
                print(comic)
