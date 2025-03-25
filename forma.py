class Forma:
    def __init__(self):
        self.orientaciones = []

    def agregarOrientacion(self, orientacion):
        self.orientaciones.append(orientacion)

    def eliminarOrientacion(self, orientacion):
        self.orientaciones.remove(orientacion)

    def ponerElementoEnOrientacion(self, elemento, orientacion):
        orientacion.poner(elemento, self)

    def obtenerElementoEnOrientacion(self, orientacion):
        return orientacion.obtenerElemento(self)
