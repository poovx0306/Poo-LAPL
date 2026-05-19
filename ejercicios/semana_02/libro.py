class Libro:
    def __init__(self, titulo, autor, editorial, genero, anio_publicacion, cantidad_paginas, ubicacion, idioma, edicion, peso):
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.genero = genero
        self.anio_publicacion = anio_publicacion
        self.cantidad_paginas = cantidad_paginas
        self.ubicacion = ubicacion
        self.idioma = idioma
        self.edicion = edicion
        self.peso = peso

        print(f"Titulo : {self.titulo}")
        print(f"Autor : {self.autor}")
        print(f"Editorial: {self.editorial}")
        print(f"Género: {self.genero}")
        print(f"Año de publicación: {self.anio_publicacion}")
        print(f"Cantidad de páginas: {self.cantidad_paginas}")
        print(f"Ubicación: {self.ubicacion}")
        print(f"Idioma: {self.idioma}")
        print(f"Edición: {self.edicion}")
        print(f"Peso: {self.peso}")

    def prestar(self):
        print(f"Método prestar")

    def renovar(self):
        print(f"Método renovar")

    def sancionar(self):
        print(f"Método sancionar")

    def devolver(self):
        print(f"Método devolver")

    def ubicar(self):
        print(f"Método ubicar")

# Creación del objeto (Instanciación)
mi_libro = Libro("Cien años de soledad", "Gabriel García Márquez", "Editorial Diana", "Novela", 1967, 496, "Estante M-3", "Español", "1ra edición", "5")