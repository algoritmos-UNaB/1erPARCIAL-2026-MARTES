from datetime import date
class Comic:
    def __init__(self,titulo:str,idcomic:int,fecha_estreno:date,precio:float,stock:int):
        self.titulo=titulo
        self.idcomic=idcomic
        self.fecha_estreno=fecha_estreno
        self.precio=precio
        self.stock=stock
    def modificar_datos(self,titulo=None,precio=None,stock=None):
        if titulo is not None:
            self.titulo=titulo
        if precio is not None:
            self.precio=precio
        if stock is not None:
            self.stock=stock
    def dias_lanzado(self,fecha_ref=None):
        if fecha_ref is None:
            fecha_ref=date.today()
        if self.fecha_estreno<fecha_ref:
            print(f'El comic {self.titulo} es más antiguo que la fecha de referencia')
            self.stock=0
            return None
        else:
            dif=self.fecha_estreno-fecha_ref
            return dif.days
    def __str__(self):
        return f'Cómic: {self.titulo}, ID: {self.idcomic}, precio: {self.precio}, stock: {self.stock}'
    def __eq__(self,other):
        return self.idcomic=other.idcomic and self.titulo==other.titulo