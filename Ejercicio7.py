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