from datetime import date

class Comic:
    def __init__(self, titulo:str, id_comic:int, fecha_publicacion:date, precio:float, stock:int):
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
        
    def calcular_dias_desde_fecha(self, fecha_referencia: date):
        dias = (fecha_referencia - self.fecha_publicacion).days
        if dias > 0:
            print(f"El comic '{self.titulo}' es mas antiguo que la fecha de referencia. Stock actualizado a 0.") 
            self.stock = 0
        return abs(dias)

#ejercicio 8

    def __str__(self):
        return f"Comic: {self.titulo} | ID: {self.id_comic} | Precio: ${self.precio:.2f} | Stock: {self.stock}"
    
    def __eq__(self, otro_comic):
        if isinstance(otro_comic, Comic):
            return self.id_comic ==otro_comic.id_comic and self.titulo == otro_comic.titulo
        return False