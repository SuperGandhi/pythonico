class Marino:
    
    def talk(self):
        print("Hola soy...")


class Pulpo(Marino):
    
    def message_pulpo(self):
        print("un pulpo")


class Foca(Marino):
    
    def talk(self, message):
        self.message = message
        print(self.message)


pulpo = Pulpo()
pulpo.talk()

foca = Foca()
foca.talk("Hola soy una foca...")
