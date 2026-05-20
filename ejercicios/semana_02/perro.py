class Perro: 
    def __init__(self, color, altura, anchura, raza, genero, dueno, peso, tipo_pelo, edad, nombre):
        self.color = color
        self.altura = altura
        self.anchura = anchura
        self.raza =  raza
        self.genero = genero
        self.dueno = dueno
        self.peso = peso
        self.tipo_pelo = tipo_pelo
        self.edad = edad
        self.nombre = nombre

        print(f"Color: {self.color}")
        print(f"Altura: {self.altura}")
        print(f"Anchura: {self.anchura}")
        print(f"Raza: {self.raza}")
        print(f"Genero: {self.genero}")
        print(f"Dueño: {self.dueno}")
        print(f"Peso: {self.peso}")
        print(f"Tipo de pelo: {self.tipo_pelo}")
        print(f"Edad: {self.edad}")
        print(f"Nombre: {self.nombre}")
    
    def Ladrar(self):
        print(f"El perro puede ladrar")
    def Comer(self):
        print(f"El perro puede comer")
    def Correr(self):
        print(f"El perro puede correr")
    def Dormir(self):
        print(f"El perro puede dormir")
    def Jugar(self):
        print(f"El perro puede jugar")

Chihuahua_chafa = Perro ("Miel", "43 cm", "25 cm ", "Chihuahua", "Macho", "Povedano", "5Kg", "Liso", "4 años", "Luca")
        
    