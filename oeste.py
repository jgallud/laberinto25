from orientacion import Orientacion
from point import Point
class Oeste(Orientacion):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def poner(self, elemento, contenedor):
        contenedor.oeste = elemento

    def recorrer(self, func, contenedor):
        if contenedor.oeste is not None:
            func(contenedor.oeste)

    def __str__(self):
        return "Soy la orientacion oeste"

    def obtenerElemento(self, forma):
        return forma.oeste

    def caminarAleatorio(self, bicho, forma):
        forma.oeste.entrar(bicho)

    def aceptar(self, unVisitor, forma):
        forma.oeste.aceptar(unVisitor)
    def calcularPosicionDesde(self, forma):
        unPunto=Point(forma.punto.x-1,forma.punto.y)
        forma.oeste.calcularPosicionDesdeEn(forma,unPunto)