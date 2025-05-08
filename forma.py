import random
class Forma:
    def __init__(self):
        self.orientaciones = []
        self.num=None
        self.punto=None
        self.extent=None

    def agregarOrientacion(self, orientacion):
        self.orientaciones.append(orientacion)

    def eliminarOrientacion(self, orientacion):
        self.orientaciones.remove(orientacion)

    def ponerElementoEnOrientacion(self, elemento, orientacion):
        orientacion.poner(elemento, self)

    def obtenerElementoEnOrientacion(self, orientacion):
        return orientacion.obtenerElemento(self)

    def recorrer(self, func):
        for orientacion in self.orientaciones:
            orientacion.recorrer(func, self)
    def calcularPosicion(self):
        for orientacion in self.orientaciones:
            orientacion.calcularPosicionDesde(self)
    def caminarAleatorio(self, bicho):
        orientacion=self.obtenerOrientacionAleatoria()
        print(f"Orientacion aleatoria: {orientacion}")
        orientacion.caminarAleatorio(bicho, self)

    def obtenerOrientacionAleatoria(self):
        return random.choice(self.orientaciones)

    def aceptar(self, unVisitor):
        for orientacion in self.orientaciones:
            orientacion.aceptar(unVisitor, self)
