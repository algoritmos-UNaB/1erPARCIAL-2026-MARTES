#El inventario de comics de Stuart.
from datetime import date

class Comic(object):
    def __init__(self, titulo, id_comic, fecha_publicacion, precio, stock):
        self.titulo = titulo
        self.id_comic = id_comic
        self.fecha_publicacion = fecha_publicacion
        self.precio = precio
        self.stock = stock
    def cambiar_datos(self, titulo = None, precio = None, stock = None):
        if titulo is not None:
            self.titulo = titulo
        if precio is not None:
            self.precio = precio
        if stock is not None:
            self.stock = stock
    def dias_desde_referencia(self, fecha_referencia):
        dias = (self.fecha_publicacion - fecha_referencia).days
        if dias < 0:
            print ("Aviso:", self.titulo, "es más antiguo que la fecha de referencia. Stock en 0.")
            self.stock = 0
        return dias

#La etiqueta de los comics.
    def __str__(self):
        return ("Comic: " + self.titulo + " | Id: " + str(self.id_comic) + " | Precio: $" + str(self.precio) + " | Stock: " + str(self.stock))
    def __eq__(self, other):
        if not isinstance (other, Comic):
            return False
        return self.id_comic == other.id_comic and self.titulo == other.titulo
        