from datetime import date

class Comic:
    def __init__(self, titulo, idcomic, fechapublicacion, precio, stock):
        self.titulo = titulo
        self.idcomic = idcomic
        self.fechapublicacion = fechapublicacion
        self.precio = precio
        self.stock = stock

    def cambiar_datos(self, titulo=None, precio=None, stock=None):
        if titulo is not None:
            self.titulo = titulo
        if precio is not None:
            self.precio = precio
        if stock is not None:
            self.stock = stock

    def dias_desde_publicacion(self, fecha_referencia):
        if self.fechapublicacion < fecha_referencia:
            print("El cómic es anterior a la fecha de referencia.")
            self.stock = 0

        return (fecha_referencia - self.fechapublicacion).days