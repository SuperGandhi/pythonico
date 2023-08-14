class Universidad:
    def __init__(self, nombre_universidad):
        self.nombre_universidad = nombre_universidad

class Carrera:
    def __init__(self, especialidad):
        self.especialidad = especialidad

class Estudiante(Carrera, Universidad):
    def __init__(self, nombre_estudiante, nombre_universidad, especialidad, edad):
        Universidad.__init__(self, nombre_universidad)
        Carrera.__init__(self, especialidad)
        self.nombre_estudiante = nombre_estudiante
        self.edad = edad

    def __str__(self):
        return f"Mi nombre es {self.nombre_estudiante}, soy de la universidad de {self.nombre_universidad}, estoy en la especialidad de {self.especialidad} y tengo {self.edad} años"

persona = Estudiante("Julian", "UCSM", "TICS", 25)
print(persona)


