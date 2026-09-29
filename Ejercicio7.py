from datetime import datetime, date

class Comic:

    def __init__(self, titulo, id_comic, fecha_publicacion, precio, stock):
        self.titulo = titulo
        self.id_comic = id_comic
        self.fecha_publicacion = fecha_publicacion 
        self.precio = float(precio)
        self.stock = int(stock)

    def modificar_datos(self, titulo=None, precio=None, stock=None):

        if titulo is not None:
            self.titulo = titulo
        if precio is not None:
            self.precio = float(precio)
        if stock is not None:
            self.stock = int(stock)

    def dias_desde_publicacion(self, fecha_referencia):

        diferencia = fecha_referencia - self.fecha_publicacion
        
        if self.fecha_publicacion < fecha_referencia:
            print(f"Aviso: El cómic '{self.titulo}' es más antiguo que la fecha de referencia.")
            self.stock = 0
            
        return abs(diferencia.days)

# Ejercicio 8

# Sobrecarga de la función print() y str()

    def __str__(self):
        return f"Comic: {self.titulo} | ID: {self.id_comic} | Precio: ${self.precio} | Stock: {self.stock}"

    def __eq__(self, otro):
        if type(otro) != type(self):
            raise NotImplementedError('No se puede comparar un Comic con un ' + str(type(otro)))
        
        return (self.id_comic == otro.id_comic) and (self.titulo == otro.titulo)