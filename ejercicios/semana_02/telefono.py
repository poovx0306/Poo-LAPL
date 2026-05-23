class Telefono:
    def __init__(self,ram,almacenamiento,capacidad_pila,mpx_camara,altura_pantalla,anchura_pantalla,camaras,resolucion,resistencia_agua,largo_telefono):
        self.ram = ram
        self.almacenamiento = almacenamiento
        self.capacidad_pila = capacidad_pila
        self.mpx_camara = mpx_camara
        self.altura_pantalla = altura_pantalla
        self.anchura_pantalla = anchura_pantalla
        self.camaras = camaras
        self. resolucion = resolucion
        self.resistencia_agua = resistencia_agua
        self.largo_telefono = largo_telefono

        print(f"Almacenamiento RAM: {self.ram}")
        print(f"Almacenamiento: {self.almacenamiento}")
        print(f"Capacidad de la pila: {self.capacidad_pila}")
        print(f"Megapixeles de la cámara: {self.mpx_camara}")
        print(f"Altura de la pantalla: {self.altura_pantalla}")
        print(f"Anchura de la pantalla: {self.anchura_pantalla}")
        print(f"Número de cámaras: {self.camaras}")
        print(f"Resolución: {self.resolucion}")
        print(f"Resistencia al agua: {self.resistencia_agua}")
        print(f"Largo del teléfono: {self.largo_telefono}")

    def ver_videos(self):
        print(f"Se pueden ver videos")

    def jugar(self):
        print(f"Se puede jugar")

    def crear_documentos(self):
        print(f"Se pueden crear documentos")

    def tomar_fotos(self):
        print(f"Se pueden tomar fotos")

    def reproducir_musica(self):
        print(f"Se puede reproducir música")

SamsungS26Ultra = Telefono ( 
    "16GB",
    "1Tb",
    "5000 Mhp",
    "200 mpx",
    "16.2 cm",
    "7.9 cm",
    "4",
    "QHD+ (3120 x 1440)",
    "IP68",
    "16.23 cm"
)

SamsungS26Ultra.crear_documentos
SamsungS26Ultra.jugar
SamsungS26Ultra.reproducir_musica
SamsungS26Ultra.ver_videos
SamsungS26Ultra.tomar_fotos