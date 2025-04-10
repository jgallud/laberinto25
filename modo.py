class Modo:
    def __init__(self):
        pass

    def actuar(self, bicho):
        self.dormir(bicho)
        self.caminar(bicho)
        self.atacar(bicho)

    def dormir(self, bicho):
        pass

    def caminar(self, bicho):
        bicho.caminar()

    def atacar(self, bicho):
        bicho.atacar()

    def __str__(self):
        return "Soy un modo"
