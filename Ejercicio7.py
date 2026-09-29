from datetime import date


class Comic:
    def __init__(self, titulo, id_comic, fecha_publicacion, precio, stock):
        self.titulo = titulo
        self.id_comic = id_comic
        self.fecha_publicacion = fecha_publicacion
        self.precio = precio
        self.stock = stock

    def cambiar_datos(self, titulo=None, precio=None, stock=None):
        if titulo is not None:
            self.titulo = titulo
        if precio is not None:
            self.precio = precio
        if stock is not None:
            self.stock = stock

    def calcular_antiguedad(self, fecha_referencia):
        dias = (fecha_referencia - self.fecha_publicacion).days

        if dias > 0:
            print("El cómic es más antiguo que la fecha de referencia.")
            self.stock = 0

        return dias

        def __str__(self):
        return f"Comic: {self.titulo} | ID: {self.id_comic} | Precio: ${self.precio} | Stock: {self.stock}"

    def __eq__(self, otro):
        return self.id_comic == otro.id_comic and self.titulo == otro.titulo