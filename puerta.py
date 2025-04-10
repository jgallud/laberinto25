from elemento_mapa import ElementoMapa
from estado_puerta import Cerrada

class Puerta(ElementoMapa):
    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2
        self.estadoPuerta = Cerrada()

    def entrar(self, alguien):
        self.estadoPuerta.entrar(self, alguien)

    def puedeEntrar(self, alguien):
        print("Entrando en una puerta")
        if alguien.posicion == self.lado1:
            self.lado2.entrar(alguien)
        else:
            self.lado1.entrar(alguien)

    def abrir(self):
        print("Abriendo puerta")
        self.estadoPuerta.abrir(self)

    def cerrar(self):
        print("Cerrando puerta")
        self.estadoPuerta.cerrar(self)

    def esPuerta(self):
        return True

    def __str__(self):
        return "Soy una puerta"
