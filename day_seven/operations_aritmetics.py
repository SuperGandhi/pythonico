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
        return self.a / self.b
    

result = Calculator(10, 20)
print(result.suma())