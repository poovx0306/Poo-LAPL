class Alumno: 
    def __init__ (self, nombre, edad, matricula, carrera, semestre, promedio, turno, universidad, correo, materia_fav):
        self.nombre = nombre
        self.edad = edad
        self.matricula = matricula
        self.carrera = carrera
        self.semestre = semestre
        self.promedio = promedio
        self.turno = turno
        self.universidad = universidad
        self.correo = correo
        self.materia_fav = materia_fav

        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Matricula: {self.matricula}")
        print(f"Carrera: {self.carrera}")
        print(f"Semestre: {self.semestre}")
        print(f"Promedio: {self.promedio}")
        print(f"Turno: {self.turno}")
        print(f"Universidad:{self.universidad}")
        print(f"Correo: {self.correo}")
        print(f"Materia Favorita:{self.materia_fav}")

    def Reprobar(self):
        print(f"El alumno puede reprobar")
    def Aprobar(self):
        print(f"El alumno puede aprobar")
    def Estudiar(self):
        print(f"El alumno puede estudiar")
    def Preguntar(self):
        print(f"El alumno puede preguntar dudas")
    def Hacer_examen(self):
        print(f"El alumno puede hacer un examen")

Alumno_1 = Alumno ("Emmanuel", "20 años", "172511234", "TIC's", "3ro", "6.7", "Matutino", "Utec", "172511234@utectulancingo.edu.mx", "Recreo")

Alumno_1.Reprobar()
Alumno_1.Aprobar()
Alumno_1.Estudiar()
Alumno_1.Preguntar()
Alumno_1.Hacer_examen()
