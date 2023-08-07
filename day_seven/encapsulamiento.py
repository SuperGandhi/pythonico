class Protein:
    def __init__(self, amino1, amino2, enlace_peptidico, dipeptido, agua):
        self._amino1 = amino1
        self._amino2 = amino2
        self._enlace_peptidico = enlace_peptidico
        self._dipeptido = dipeptido
        self._agua = agua

    @property
    def amino1(self):
        return self._amino1

    @amino1.setter
    def amino1(self, value):
        self._amino1 = value

    @property
    def amino2(self):
        return self._amino2

    @amino2.setter
    def amino2(self, value):
        self._amino2 = value

    @property
    def enlace_peptidico(self):
        return self._enlace_peptidico

    @enlace_peptidico.setter
    def enlace_peptidico(self, value):
        self._enlace_peptidico = value

    @property
    def dipeptido(self):
        return self._dipeptido

    @dipeptido.setter
    def dipeptido(self, value):
        self._dipeptido = value

    @property
    def agua(self):
        return self._agua

    @agua.setter
    def agua(self, value):
        self._agua = value

    def listado(self):
        print(f"Las proteinas se componen de : {self._amino1}, {self._amino2}, {self._enlace_peptidico}, {self._dipeptido} y {self._agua}")


message = Protein("amino1", "amino2", "enlace peptidico", "dipeptido", "agua")

message.amino1 = "amino1 actualizado"
message.amino2 = "amino2 actualizado"
message.enlace_peptidico = "enlace peptidico actualizado"
message.dipeptido = "dipeptido actualizado"
message.agua = "agua actualizada"

message.listado()
