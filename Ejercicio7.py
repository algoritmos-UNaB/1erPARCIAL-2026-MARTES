from datetime import datetime

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
        else:
            pass

    def dias_publicacion(self, fecha_referencia):
        diferencia = fecha_referencia - self.fecha_publicacion

        if self.fecha_publicacion < fecha_referencia:
            print("El comic es mas antiguo que la fecha de referencia")
            self.stock = 0

        return diferencia.days

    def __str__(self):
        return f"Comic: {self.titulo} | ID: {self.id_comic} | Precio: ${self.precio} | Stock: {self.stock}"

    def __eq__(self, alt_comic):
        return self.id_comic == alt_comic.id_comic and self.titulo == alt_comic.titulo