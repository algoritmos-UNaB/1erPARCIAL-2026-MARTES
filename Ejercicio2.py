#Nombre y apellido: Leandro Leonel Veliz
#Email: leandro.leonel.veliz@gmail.com
#Comisión: 3

class Biblioteca:

    # EJERCICIO 2: La Biblioteca de Sheldon
    
    def __init__(self):
        """Crea una biblioteca vacía utilizando una lista."""
        self.libros = [] 

    def esta_vacia(self):
        """Identifica si una biblioteca está vacía o no."""
        return len(self.libros) == 0 

    def anadir_libro(self, libro):
        """Añade un libro de la biblioteca."""
        self.libros.append(libro) 

    def remover_libro(self, libro):
        """Remueve un libro de la biblioteca."""
        if libro in self.libros:
            self.libros.remove(libro) 
        else:
            print(f"El libro '{libro}' no se encuentra en la biblioteca.")

    # EJERCICIO 3: La Organización de la Biblioteca

    def leer_primer_libro(self):
        """Retorna el primer libro de la colección."""
        if not self.esta_vacia():
            return self.libros[0] 
        return None

    def leer_ultimo_libro(self):
        """Retorna el último libro de la colección."""
        if not self.esta_vacia():
            return self.libros[-1] 
        return None

    def insertar_al_principio(self, libro):
        """Inserta un libro en la primera posición (índice 0)."""
        self.libros.insert(0, libro) 

    def agregar_al_final(self, libro):
        """Agrega un libro al final de la colección."""
        self.libros.append(libro) 

    # EJERCICIO 4: La Representación de la Biblioteca

    def __len__(self):
        """Sobrescribe el método len() para devolver la cantidad de libros."""
        return len(self.libros) 

    def __str__(self):
        """Sobrescribe la representación en texto (str) de la clase."""
        if self.esta_vacia():
            return "La biblioteca está vacía." 
        return f"Biblioteca ({len(self.libros)} libros): " + ", ".join(self.libros) 

    def __eq__(self, otra_biblioteca):
        """Compara si dos bibliotecas son exactamente iguales."""
        if isinstance(otra_biblioteca, Biblioteca):
            return self.libros == otra_biblioteca.libros 
        return False

    def __add__(self, otra_biblioteca):
        """Permite sumar (+) dos bibliotecas uniendo sus colecciones."""
        if isinstance(otra_biblioteca, Biblioteca):
            nueva_biblio = Biblioteca() 
            # Sumamos las listas de libros de ambas bibliotecas
            nueva_biblio.libros = self.libros + otra_biblioteca.libros 
            return nueva_biblio
        raise TypeError("Solo se pueden sumar objetos del tipo Biblioteca") 