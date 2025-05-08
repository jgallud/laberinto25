from orientacion import Orientacion
from point import Point
class Norte(Orientacion):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def poner(self, elemento, contenedor):
        contenedor.norte = elemento

    def recorrer(self, func, contenedor):
        if contenedor.norte is not None:
            func(contenedor.norte)

    def __str__(self):
        return "Soy la orientacion norte"

    def obtenerElemento(self, forma):
        return forma.norte

    def caminarAleatorio(self, bicho, forma):
        forma.norte.entrar(bicho)

    def aceptar(self, unVisitor, forma):
        forma.norte.aceptar(unVisitor)
    def calcularPosicionDesde(self, forma):
        unPunto=Point(forma.punto.x,forma.punto.y-1)
        forma.norte.calcularPosicionDesdeEn(forma,unPunto)