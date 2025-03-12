from contenedor import Contenedor

class Habitacion(Contenedor):
    def __init__(self, num):
        super().__init__()
        self.num = num

    def entrar(self, alguien):
        print(f"Entrando en la habitación {self.num}")
        alguien.posicion=self

    def __str__(self):
        return "Soy una habitacion"
