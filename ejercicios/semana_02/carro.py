class Carro:
    def __init__(self, marca, modelo, placa, color, anio, kilometraje, transmision, puertas, combustible, ubicacion):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.color = color
        self.anio = anio
        self.kilometraje = kilometraje
        self.transmision = transmision
        self.puertas = puertas
        self.combustible = combustible
        self.ubicacion = ubicacion

        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Placa: {self.placa}")
        print(f"Color: {self.color}")
        print(f"Año: {self.anio}")
        print(f"Kilometraje: {self.kilometraje}")
        print(f"Transmisión: {self.transmision}")
        print(f"Puertas: {self.puertas}")
        print(f"Combustible: {self.combustible}")
        print(f"Ubicación: {self.ubicacion}")

    def encender(self):
        print(f"Método encender")

    def acelerar(self):
        print(f"Método acelerar")

    def frenar(self):
        print(f"Método frenar")

    def estacionar(self):
        print(f"Método estacionar")

    def ubicar(self):
        print(f"Método ubicar")

# Creación del objeto (Instanciación)
m1_carro = Carro("Mazda", "3", "XYZ-789", "Azul", 2023, "12,000 km", "Automático", 4, "Gasolina", "Estación B-2")