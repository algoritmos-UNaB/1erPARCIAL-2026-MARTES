from Ejercicio7 import Comic

class TiendaComics:
    def __init__(self):
        self.secciones = {
            "DC Comics": [],
            "Marvel": [],
            "Independientes": []
        }

    def agregar_comic(self, seccion: str, comic: Comic):
        