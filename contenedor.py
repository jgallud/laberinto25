from elemento_mapa import ElementoMapa

class Contenedor(ElementoMapa):
    def __init__(self):
        super().__init__()
        self.hijos = []
        self.forma = None

    def agregar_hijo(self, hijo):
        hijo.padre = self
        self.hijos.append(hijo)

    def eliminar_hijo(self, hijo):
        self.hijos.remove(hijo)

    def agregarOrientacion(self, orientacion):
        self.forma.agregarOrientacion(orientacion)

    def eliminarOrientacion(self, orientacion):
        self.forma.eliminarOrientacion(orientacion)

    def ponerElementoEnOrientacion(self, elemento, orientacion):
        self.forma.ponerElementoEnOrientacion(elemento, orientacion)

    def recorrer(self, func):
        func(self)
        for hijo in self.hijos:
            hijo.recorrer(func)
        self.forma.recorrer(func)

    def obtenerElementoEnOrientacion(self, orientacion):
        return self.forma.obtenerElementoEnOrientacion(orientacion)
    
    def caminarAleatorio(self, bicho):
        self.forma.caminarAleatorio(bicho)

    def aceptar(self, unVisitor):
        self.visitarContenedor(unVisitor)
        for hijo in self.hijos:
            hijo.aceptar(unVisitor)
        self.forma.aceptar(unVisitor)
