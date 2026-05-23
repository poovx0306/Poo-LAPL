class Silla:
    def __init__(self, color, anchura, altura, forma, material, peso_max,estilo,patas,marca,respaldo):
        self.color = color
        self.anchura = anchura
        self.altura = altura
        self.forma = forma
        self.material = material
        self.peso_max = peso_max
        self.estilo = estilo
        self.patas = patas
        self.marca = marca
        self.respaldo = respaldo

        print(f"Color: {self.color}")
        print(f"Anchura: {self.anchura}")
        print(f"Altura: {self.altura}")
        print(f"Forma: {self.forma}")
        print(f"Material: {self.material}")
        print(f"Peso Maximo: {self.peso_max}")
        print(f"Estilo: {self.estilo}")
        print(f"Número de patas: {self.patas}")
        print(f"Marca: {self.marca}")
        print(f"Respaldo: {self.respaldo}")

    def sentarse(self):
        print(f"Se pueden sentar")
    
    def limpiar(self):
        print(f"Se puede limpiar")
              
    def mover(self):
        print(f"Se puede mover")
    
    def girar(self):
        print(f"Se puede mover")
    
    def desarmar(self):
        print(f"Se puede desarmar")

SillaLaboratorio = Silla ("Blanca" , 
                          "30cm",
                          "50cm",
                          "Rectangular",
                          "Metal",
                          "100 kg",
                          "Moderno",
                          "2",
                          "IKEA",
                          "Rectangular")
                        