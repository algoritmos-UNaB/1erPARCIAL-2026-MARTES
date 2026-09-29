import datetime

class comic:
    def __init__(self, titulo:str, id_comic:int, fecha_publicacion: datetime.date, precio: float, stock: int):
        self.titulo= titulo
        self.id_comic= id_comiv
        self.fecha_publicacion= fecha_publicacion
        self.precio= precio
        self.stock= stock

    def cambiar_titulo(sel,nuevo_titulo: str):
        self.titulo = nuevo.titulo
    def cambiar_precio(self, nuevo_precio: float):
        self.precio = nuevo_precio
    def cambiar_stock(self, nuevo_stock: int):
        self.stock= nuevo_stock

    def dias_desde_publicacion(self, fecha_referencia: datetime.date):
        if self.fecha_publicacion < fecha_referencia:
            self_stock = 0
        else:
            diferencia= self.fecha_publicacion - fecha_referencia
            return diferencia.days 
    #ejercicio 8
    def __str__(self):
        return f"Comic: {self.titulo} | ID:{self.id_comic} | Precio: ${self.precio} | Stock: {self.stock}"

    def __eq__(self, otro_comic):
        if isinstance(otro_comic, Comic):
            return self.id_comic == otro_comic.id_comic and self.titulo == otro_comic.titulo
        else: False