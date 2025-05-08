from decorator import Decorator

class Bomba(Decorator):
    def __init__(self, em):
        super().__init__(em)
        self.activa = False

    def esBomba(self):
        return True

    def aceptar(self, unVisitor):
        unVisitor.visitarBomba(self)
    
    def __str__(self):
        return "Soy una bomba"
