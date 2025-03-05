from modo import Modo

class Perezoso(Modo):
    def __init__(self):
        super().__init__()

    def dormir(self, bicho):
        print("Perezoso: Zzzzz...")

    def caminar(self, bicho):
        print("Perezoso: Caminando sin ganas...")

    def atacar(self, bicho):
        print("Perezoso: Intentando atacar...")
