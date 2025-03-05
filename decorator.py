from hoja import Hoja

class Decorator(Hoja):
    def __init__(self, em):
        super().__init__()
        self.em = em

    def __str__(self):
        return "Soy un decorator"
