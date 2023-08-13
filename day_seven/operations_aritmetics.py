class Calculator:
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def suma(self):
        return self.a + self.b
    
    def resta(self):
        return self.a - self.b
    
    def multiplicación(self):
        return self.a * self.b
    
    def division(self):
        try:
            return self.a / self.b
        except ZeroDivisionError:
            return "No puedes dividir por cero"

result = Calculator(20, 0)
print(result.division())