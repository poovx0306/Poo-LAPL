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
                                                                                                                                                                            
                                                                                                                                                                                def cargar():
                                                                                                                                                                                        print(f"La mesa carga.")
                                                                                                                                                                                            
                                                                                                                                                                                                def limpiar():
                                                                                                                                                                                                        print(f"La mesa puede ser limpiada.")
                                                                                                                                                                                                            
                                                                                                                                                                                                                def mover():
                                                                                                                                                                                                                        print(f"La mesa se puede cargar.")

                                                                                                                                                                                                                            def plegar():
                                                                                                                                                                                                                                    print(f"La mesa puede ser plegada.")

                                                                                                                                                                                                                                        def desplegar():
                                                                                                                                                                                                                                                print(f"La mesa puede ser desplegada.")

                                                                                                                                                                                                                                                mesa_laboratorio=Mesa(
                                                                                                                                                                                                                                                    "Blanca", 
                                                                                                                                                                                                                                                        "10 cm",
                                                                                                                                                                                                                                                            "25 cm", 
                                                                                                                                                                                                                                                                "Circular", 
                                                                                                                                                                                                                                                                    "Madera",
                                                                                                                                                                                                                                                                        "100 Kg",
                                                                                                                                                                                                                                                                            "Elegante",
                                                                                                                                                                                                                                                                                "4",
                                                                                                                                                                                                                                                                                    "IKEA",
                                                                                                                                                                                                                                                                                        "120 cm")