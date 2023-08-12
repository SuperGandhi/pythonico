class Estudiante:
        
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        
    def resultado_nota(self):
        if self.grade >= 12:
            print(f"Hola {self.name} quiero informarte que aprobaste con : {self.grade}")
        else:
            print(f"Hola {self.name} lamentamos informarte que no aprobaste tu nota es : {self.grade}")


        
student = Estudiante("Mario", 12)
student.resultado_nota()


