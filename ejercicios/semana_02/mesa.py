class Mesa:
        def __init__(self, color, anchura, altura, forma, material, peso_max, estilo, patas, marca, largo):
                self.color = color
                self.anchura = anchura
                self.altura = altura
                self.forma = forma
                self.material = material
                self.peso_max = peso_max
                self.estilo = estilo                                                                                                                
                self.patas = patas
                self.marca = marca
                self.largo = largo                                
                                
                print(f"Color: {self.color}")
                print(f"Anchura: {self.anchura}")
                print(f"Altura: {self.altura}")
                print(f"Forma: {self.forma}")
                print(f"Material: {self.material}")
                print(f"Peso máximo: {self.peso_max}")
                print(f"Estilo: {self.estilo}")
                print(f"Numero de patas: {self.patas}")
                print(f"Marca: {self.marca}")
                print(f"Largo: {self.largo}")
                                
        def cargar(self):

                print(f"La mesa carga.")    

        def limpiar(self):
                print(f"La mesa puede ser limpiada")
                
        def mover(self):
                print(f"La mesa se puede mover")
        
        def plegar(self):
                print(f"La mesa se puede plegar")

        def desplegar(self):
                print(f"La mesa puede ser desplegada")

mesa_laboratorio = Mesa ("Blanca", "1.5 mtrs", "1.20 mtrs", "Renctangular", "Madera", "150 Kg", "Moderna", "4", "IKEA", "1.20 mtrs")

mesa_laboratorio.cargar()
mesa_laboratorio.limpiar()
mesa_laboratorio.mover()
mesa_laboratorio.plegar()
mesa_laboratorio.desplegar()
