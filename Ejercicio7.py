import datetime as dt
class Comic:
    def __init__(self, titulo: str, id_comic: int, fecha_publicacion: dt.date, precio: float, stock: int):
        self._titulo = titulo
        self._id_comic = int(id_comic)
        self._fecha_publicacion = fecha_publicacion
        self._precio = precio
        self._stock = stock
    
    def modificar_dato(self, titulo = None, )

