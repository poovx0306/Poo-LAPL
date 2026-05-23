class Universidad: 
    def __init__(self, logo, oferta_educativa, localidad, sistema_informacion, modalidad, servicios, ubicacion, talleres, cantidad_salones, rector):
        self.logo = logo
        self.oferta_educativa = oferta_educativa
        self. localidad = localidad
        self. sistema_informacion = sistema_informacion
        self. modalidad = modalidad
        self. servicios = servicios
        self. ubicacion = ubicacion
        self. talleres = talleres
        self. cantidad_salones = cantidad_salones
        self. rector = rector
        print (f"Logo: {self.logo}")
        print (f"Oferta Educativa {self.oferta_educativa}")
        print (f"Localidad {self.localidad}")
        print (f"Sistema de Información: {sistema_informacion}")
        print (f"Modalidad {modalidad}")
        print (f"Servicios {servicios}")
        print (f"Ubicacion {ubicacion}")
        print (f"Talleres {talleres}")
        print (f"Cantidad de salones: {cantidad_salones}")
        print (f"Rector: {rector}")

    def incribir(self):
        print(f"Se pueden inscribir en la universidad")
    def realizar_eventos(self):
        print(f"La universidad puede realizar eventos")
    def realizar_graduacion(self):
            print("Se está llevando a cabo la ceremonia de graduación de la generación saliente.")

    def abrir_biblioteca(self):
            print("La biblioteca central ha abierto sus puertas para que los alumnos estudien.")

    def organizar_evento(self):
            print("Se está organizando una feria de proyectos de software y tecnología en el campus.")    

utec = Universidad("logo.jpg", "TICs, Contaduria", "Santiago", "SII", "Presencial", "Becas, talleres", "Ahuehuetitla", "Artes visuales, popotillo", 54, "Tito Dorante")
                                                                                                                                                                                                     
        


                