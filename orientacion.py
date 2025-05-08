class Orientacion:
    def __init__(self):
        pass

    def poner(self, elemento, contenedor):
        pass

    def recorrer(self, func, forma):
        raise NotImplementedError

    def __str__(self):
        return "Soy una orientacion"

    def obtenerElemento(self, forma):
        raise NotImplementedError
    def caminarAleatorio(self, bicho, forma):
        raise NotImplementedError
    def aceptar(self, unVisitor, forma):
        raise NotImplementedError
    def calcularPosicionDesde(self, forma):
        raise NotImplementedError