class Transporte:
    def __init__(self, tipo, marca, modelo, placa, color, capacidad, anio, combustible, kilometraje, ubicacion):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.color = color
        self.capacidad = capacidad
        self.anio = anio
        self.combustible = combustible
        self.kilometraje = kilometraje
        self.ubicacion = ubicacion

        print(f"Tipo: {self.tipo}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Placa: {self.placa}")
        print(f"Color: {self.color}")
        print(f"Capacidad: {self.capacidad}")
        print(f"Año: {self.anio}")
        print(f"Combustible: {self.combustible}")
        print(f"Kilometraje: {self.kilometraje}")
        print(f"Ubicación: {self.ubicacion}")

    def encender(self):
        print(f"Método encender")

    def arrancar(self):
        print(f"Método arrancar")

    def frenar(self):
        print(f"Método frenar")

    def apagar(self):
        print(f"Método apagar")

    def ubicar(self):
        print(f"Método ubicar")

# Creación del objeto (Instanciación)
m1_transporte = Transporte("Carro", "Toyota", "Corolla", "123", "Rojo", "5 pasajeros", 2022, "Gasolina", "15,000 km", "Estacionamiento A")