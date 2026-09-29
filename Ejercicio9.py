from Ejercicio7 import Comic

class TiendaComics:
    def __init__(self):
        self.secciones = {
            "DC Comics": [],
            "Marvel": [],
            "Independientes": []
        }

    def agregar_comic(self, seccion: str, comic: Comic):
        # Agregar comic
        if seccion in self.secciones:
            self.secciones[seccion].apped(comic)
        else:
            print(f"Error: La seccion {seccion} no existe.")
    
    def remover_comic(self, comic_a_remover: Comic):
        #Remover comic
        localizado = False
        for seccion, comic in self.secciones.items():
            if comic_a_remover in comics:
                comics.remove(comic_a_remover)
                localizado = True
                print(f"Se elimino el comic {comic_a_remover}")
                break
            if not localizado:
                print("El comic no se encuentra en el inventario")

    def actualizar_stock(self, id_comic: int, nuevo_stock: int):
        # Buscar comic y modificar su stock
        for seccion, comic in self.secciones.items():
            for comic in comics:
                if comic.id_comic == id_comic:
                    comic.stock = nuevo_stock
                    print(f"Stock de {comic.titulo} actualizado a {nuevo_stock}.")
        else:
            print("No se encontro ningun comic con ese ID.")

    def retirar_stock_critico(self):
        # Si el stock calculado es menor o igual a 3, se remueven del inventario
        total_removidos = 0
        
        for seccion, comics in self.secciones.items():
            # Filtrar comics que se mantienen
            comics_a_conservar = []
            for comic in comics:
                if comic.stock <= 3:
                    total_removidos +=1
                else:
                    comics_a_conservar.append(comic)
        
        # Muestra los comics a conservar
            self.secciones[seccion] = comics_a_conservar
        
        print(f"Stuart retiro {total_removidos} comic/s por falta de demanda.")
        return total_removidos
    
