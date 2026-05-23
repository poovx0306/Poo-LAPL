class PersonajeVideojuego:
    def __init__(self, nombre, salud, velocidad, arma_equipada, faccion, armadura, nivel, habilidad, rol, energia):
        self.nombre = nombre
        self.salud = salud
        self.velocidad = velocidad
        self.arma_equipada = arma_equipada
        self.faccion = faccion
        self.armadura = armadura
        self.nivel = nivel
        self.habilidad = habilidad
        self.rol = rol
        self.energia = energia
        print(f"Nombre: {self.nombre}")
        print(f"Salud: {self.salud}")
        print(f"Velocidad: {self.velocidad}")
        print(f"Arma Equipada: {self.arma_equipada}")
        print(f"Facción: {self.faccion}")
        print(f"Armadura: {self.armadura}")
        print(f"Nivel: {self.nivel}")
        print(f"Habilidad: {self.habilidad}")
        print(f"Rol: {self.rol}")
        print(f"Energía: {self.energia}")

    def atacar(self):
        print(f"Puede atacar")

    def defender(self):
        print(f"Puede defenderse")

    def curar(self):
        print(f"Se puede curar")

    def saltar(self):
        print(f"Puede saltar")

    def correr(self):
        print(f"Puede correr")

heroe = PersonajeVideojuego (
    "Kael",
    "250 HP",
    "45",
    "Daga",
    "Oscuros",
    "100",
    "37",
    "Bolas de fuego oscuro",
    "Mago",
    "500")

heroe.atacar
heroe.correr
heroe.curar
heroe.defender
heroe.saltar