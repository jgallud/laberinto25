from elemento_mapa import ElementoMapa

class Pared(ElementoMapa):
    def __init__(self):
        super().__init__()

    def entrar(self,alguien):
        print("chocando en una pared")

    def __str__(self):
        return "Soy una pared"
