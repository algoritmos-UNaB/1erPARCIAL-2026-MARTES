from datetime import date

class Comic:

    def __init__(self, titulo, id_comic, fecha_publicacion, precio, stock):
        self.titulo = titulo
        self.id_comic = id_comic
        self.fecha_publicacion = fecha_publicacion
        self.precio = float(precio)
        self.stock = int(stock)

    def actualizar(self, titulo=None, precio=None, stock=None):
        if titulo is not None:
            self.titulo = titulo
        if precio is not None:
            self.precio = float(precio)
        if stock is not None:
            self.stock = int(stock) 

    def dias_desde_referencia(self, fecha_referencia: date) -> int:
        if not isinstance(fecha_referencia, date): 
            raise TypeError("fecha_referencia debe ser datetime.date")
        delta = fecha_referencia - self.fecha_publicacion
        dias = max(delta.days, 0)

        if self.fecha_publicacion < fecha_referencia:
            print(f"El cómic '{self.titulo}' (ID {self.id_comic} fue publicado hace {dias} días respecto a {fecha_referencia}. Stock marcado a 0.")
            self.stock = 0
        return dias

    # Ejercicio 8:

    def __str__(self):
        return f"Comic: {self.titulo} | ID: {self.id_comic} | Precio: ${self.precio:.2f} | Stock: {self.stock}"

    def __eq__(self, other):
        if not isinstance(other, Comic):
            return NotImplemented
        return (self.id_comic == other.id_comic) and (self.titulo == other.titulo)