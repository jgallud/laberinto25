from elemento_mapa import ElementoMapa

class Hoja(ElementoMapa):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Soy una hoja"
