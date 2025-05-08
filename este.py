from orientacion import Orientacion
from point import Point

class Este(Orientacion):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def poner(self, elemento, contenedor):
        contenedor.este = elemento

    def recorrer(self, func, contenedor):
        if contenedor.este is not None:
            func(contenedor.este)

    def __str__(self):
        return "Soy la orientacion este"

    def obtenerElemento(self, forma):
        return forma.este

    def caminarAleatorio(self, bicho, forma):
        forma.este.entrar(bicho)

    def aceptar(self, unVisitor, forma):
        forma.este.aceptar(unVisitor)
    def calcularPosicionDesde(self, forma):
        unPunto=Point(forma.punto.x+1,forma.punto.y)
        forma.este.calcularPosicionDesdeEn(forma,unPunto)