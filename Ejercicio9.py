#(2pt.) Ejercicio 9: La Gestión de la Tienda de Comics
#Crear una clase TiendaComics, la cual estará representada mediante varias listas de objetos
#del tipo Comic. Cada lista corresponde a una sección de la tienda 
#(ej: "DC Comics", "Marvel", "Independientes").

#La clase debe contener métodos para facilitar:

#Controlar el stock de cómics (añadir un nuevo cómic a una sección, remover un cómic del 
#inventario, actualizar stock). 
# funciones para : agregar, remover, actualziar stock
#Calcular cuántos cómics tienen stock crítico (menor o igual a 3) y removerlos del 
#inventario (simulando que Stuart los retira por falta de demanda).

class TiendaComics:
    def __init__(self):
        self.secciones = {
            "DC Comics": [],
            "Marvel": [],
            "Independientes": []
        }

    def agregar_comic(self, seccion, comic):
        self.secciones[seccion].append(comic)

    def remover_comic(self, seccion, comic):
        if comic in self.secciones[seccion]:
            self.secciones[seccion].remove(comic)
    
    def actualizar_stock(self, seccion, id_comic, nuevo_stock):
        for comic in self.secciones[seccion]:
            if comic.id_comic == id_comic:
                comic.stock = nuevo_stock

    def remover_stock(self):
        cant = 0

        for seccion in self.secciones:
            remover_comic = []

            for comic in self.secciones[seccion]:
            
                if comic.stock <= 3:
                    cantidad = cantidad + 1
                    remover_comic.append(comic)

            for comic in remover_comic:
                self.secciones[seccion].remove(comic)

        return cantidad

