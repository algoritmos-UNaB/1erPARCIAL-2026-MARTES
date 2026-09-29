class Biblioteca:
    def __init__(self):
        self.libros=[]
    def vacia(self):
        return len(self.libros)==0
    def libro_nuevo(self,libro):
        self.libros.append(libro)
    def borrar_libro(self,libro):
        if libro in self.libros:
            self.libros.remove(libro)
        else:
            print(f'Error: el libro {libro} no se encuentra en la biblioteca')
    def __str__(self):
        if self.vacia()
            return 'La biblioteca esta vacía'
        lista_nombres=[str(libro) for libro in self.libros]
        return f'Biblioteca con {len(self.libros)} libro/s: {', '.join(lista_nombres)}'
    def leer_1er_libro(self):
        if self.vacia():
            return 'No hay libros para leer'
        return self.libros[0]
    def leer_ultimo_libro(self):
        if self.vacia():
            return 'No hay libros para leer'
        ult=len(self.libros)-1
        return self.libros[ult]
    def agregar_primero(self,libro):
        self.libros.insert(0,libro)
    def agregar_ultimo(self,libro):
        self.libros.append(libro)
    def __len__(self):
        return len(self.libros)
    def __eq__(self,other):
        return self.libros==other.libros
    def __add__(self,other):
        nueva=Biblioteca()
        nueva.libros=self.libros.copy()+other.libros.copy()
        return nueva