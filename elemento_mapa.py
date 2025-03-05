class ElementoMapa:
    def __init__(self):
        self.padre = None
    
    def recorrer(self, func):
        func(self)

    def entrar(self):
        pass

    def esPuerta(self):
        return False

    def __str__(self):
        return "Soy un ElementoMapa"
