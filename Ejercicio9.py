class Tiendacomics:
    def __init__(self):
        self.Marvel=[]
        self.DC=[]
    def nuevo_comic(self,comic,seccion):
        if seccion=='Marvel':
            self.Marvel.append(comic)
        elif seccion=='DC':
            self.DC.append(comic)
        else:
             print('Editorial erronea o no aceptada')
    def sacar_comic(self.comic):
        if comic in self.Marvel:
            self.Marvel.remove(comic)
        elif comic in self.DC:
            self.DC.remove(comic)
        else print('El cómic no está en stock')
    def actualizar_stock(self,comic,nuevo_stock):
        comic.stock=nuevo_stock
    def limpiar_stock(self):
        total=len(self.Marvel)+len(self.DC)
        self.Marvel=[comic for comic in self.Marvel if comic.stock>3]
        self.DC=[comic for comic in self.DC if comic.stock>3]
        retirados=total-(len(self.Marvel)+len(self.DC))
        print(f'Stuart retiro {retirados} comic/s del inventario')
        return retirados