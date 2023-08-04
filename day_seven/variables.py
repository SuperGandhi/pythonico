
# Variables de instancia

class Financial:
    
    def __init__(self,assets,pasive):
        self.assets = assets
        self.pasive = pasive
        self.incomes = 0 # variable de instancia 


    def incomes_plus(self, plus):
        self.incomes += plus
    
    def bills(self, less):
        self.incomes -= less
        


julius = Financial(30,20) 

julius.incomes_plus(30)
julius.bills(50)

print(julius.assets , julius.pasive, julius.incomes)
        

# Variables de clase


class Financial:
    
    incomes = 0 # variable de clase
        
    def __init__(self,assets,pasive):
        self.assets = assets
        self.pasive = pasive
        self.incomes = 0 # variable de instancia 


    def incomes_plus(self, plus):
        self.incomes += plus
    
    def bills(self, less):
        self.incomes -= less
        


julius = Financial(30,20) 

julius.incomes_plus(30)
julius.bills(50)

print(julius.assets , julius.pasive, julius.incomes)



# Comprobando la existencia de un atributo 

class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

example_object = ExampleClass(1)

if hasattr(example_object, 'b'): 
    print(example_object.b)


