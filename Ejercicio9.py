class TiendaComics:
    def __init__(self):

        self.marvel= []
        self.dc= []
        self.independientes = []

    def anadir_comic(self, seccion: str, comic)
    if seccion == "Marvel":
        self.marvel.append(comic)
    elif seccion == "DC":
        self.DC.append(comic)
    else seccion == "Independientes":
        self.independientes.append(comic)

    def remover_comic(self, seccion: str, comic):
        if seccion == "Marvel" and comic in self.marvel:
            self.marvel.romeve(comic)
        elif seccion == "DC" and comic in self.dc:
            self.dc.remove(comic)
        else seccion == "Independientes" and comic in self.independientes:
            self.independientes.remove(comic)
        
    def actualizar_stock(self, comic, nuevos_stock: int):
        comic.stock = nuevos_stock

    def stock_critico(self):
        retirados = 0

        marvel_suficientes = []
        for comic in self.marvel:
            if comic.stock <=3
            retirados+=1
            else:
                marvel_suficientes.append(comic)
            self.marvel = marvel_suficientes

        dc_suficiente= []
        for comic in self.dc:
            if comic.stock<=3
            retirados+=1
            else:
                dc_suficiente.append(comic)
        self.dc = dc_suficiente

         independientes_suficiente= []
        for comic in self.independientes:
            if comic.stock<=3
            retirados+=1
            else:
                independientes_suficiente.append(comic)
        self.independinetes = independinetes_suficiente

        print(f"se retiraron {retirados} comic por stock critico")
        return retirados



    


