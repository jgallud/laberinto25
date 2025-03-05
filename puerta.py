from elemento_mapa import ElementoMapa

class Puerta(ElementoMapa):
    def __init__(self, lado1, lado2):
        self.abierta = False
        self.lado1 = lado1
        self.lado2 = lado2

    def entrar(self):
        print("Entrando en una puerta")

    def abrir(self):
        print("Abriendo puerta")
        self.abierta = True

    def cerrar(self):
        self.abierta = False

    def esPuerta(self):
        return True

    def __str__(self):
        return "Soy una puerta"
