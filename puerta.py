from elemento_mapa import ElementoMapa
from estado_puerta import Cerrada

class Puerta(ElementoMapa):
    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2
        self.visitada = False
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
    
    def aceptar(self, unVisitor):
        unVisitor.visitarPuerta(self)

    def calcularPosicionDesdeEn(self,forma, punto):
        print("punto: ", punto.x, punto.y)
        if self.visitada:
            return
        self.visitada = True
        if self.lado1.num == forma.num:
            self.lado2.forma.punto=punto
            self.lado2.calcularPosicion()
        else:
            self.lado1.forma.punto=punto
            self.lado1.calcularPosicion()
    
    def __str__(self):
        return "Soy una puerta"
