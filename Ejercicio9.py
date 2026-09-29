#la tienda de stuart
class TiendaComics:
    def __init__(self):
        # Uso un diccionario asi ubico las distintas secciones con sus listas de comics
        self.secciones = {
            "DC Comics": [],
            "Marvel": [],
            "Independientes": []
        }

    # 1.para agregar un nuevo comic a una seccion
    def agregar_comic(self, seccion, comic):
        if seccion in self.secciones:
            self.secciones[seccion].append(comic)
        else:
            print(f"La seccion '{seccion}' no existe.")

    # 2. Remover un comic del inventario
    def remover_comic(self, comic):
        for lista_comics in self.secciones.values():
            if comic in lista_comics:
                lista_comics.remove(comic)

    # 3. Actualizar stock de un cómic
    def actualizar_stock(self, comic, nuevo_stock):
        comic.stock = nuevo_stock

    # 4. Calcular cómics con stock crítico (<= 3) y removerlos
    def limpiar_stock_critico(self):
        cantidad_removidos = 0
        
        # Recorremos cada sección
        for seccion in self.secciones:
            # Filtramos manteniendo solo los cómics con stock mayor a 3
            libros_mantenidos = []
            for comic in self.secciones[seccion]:
                if comic.stock <= 3:
                    cantidad_removidos += 1
                else:
                    libros_mantenidos.append(comic)
            
            # Actualizamos la sección con la lista limpia
            self.secciones[seccion] = libros_mantenidos
            
        return cantidad_removidos