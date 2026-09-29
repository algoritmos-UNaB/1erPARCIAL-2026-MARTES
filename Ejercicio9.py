class TiendaComics:

    def __init__(self):
        self._secciones = {}

    def añadir_comic(self, seccion, comic):
        if seccion not in self._secciones:
            self._secciones[seccion] = []

        self._secciones[seccion].append(comic)

    def eliminar_comic(self, comic):
        for seccion, lista_comics in self._secciones.items():
            if comic in lista_comics:
                lista_comics.remove(comic) 


    def actualizar_stock(self, comic, nuevo_stock):

        comic.modificar_datos(stock=nuevo_stock)

    def eliminar_stock_critico(self):

        total_eliminados = 0
        
        for seccion, lista_comics in self._secciones.items():

            comics_a_conservar = [c for c in lista_comics if c.stock > 3]
            
            eliminados_en_seccion = len(lista_comics) - len(comics_a_conservar)
            total_eliminados += eliminados_en_seccion
            
            self._secciones[seccion] = comics_a_conservar
                
        return total_eliminados