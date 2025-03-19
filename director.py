import json
from laberinto_builder import LaberintoBuilder


class Director:
    def __init__(self, builder):
        self._builder = builder
        self.dict=None

    def procesar(self,unArchivo):
        self.leerArchivo(unArchivo)
        self.iniBuilder()
        self.fabricarLaberinto()
        self.fabricarJuego()
        self.fabricarBichos()

    def iniBuilder(self):
        self._builder=LaberintoBuilder()

    def fabricarLaberinto(self):
        self._builder.fabricarLaberinto()
        for each in self.dict['laberinto']:
            self.fabricarLaberintoRecursivo(each,'root')
        
        for each in self.dict['puertas']:
            self._builder.fabricarPuerta(each[0],each[1],each[2],each[3]) 
	
    #    "recorrer la colección de puertas, para poner las puertas"
	#(self dict at:'puertas') do:[:each | 
	#	self builder fabricarPuertaL1:(each at:1) or1:(each at:2) L2:(each at:3) or2:(each at:4)].
    
    def fabricarLaberintoRecursivo(self,each,padre):
        if each['tipo']=='habitacion':
            con=self._builder.construir_habitacion(each['numero'])
        
        if each['hijos']!=None:
            for cadaUno in each['hijos']:
                self.fabricarLaberintoRecursivo(cadaUno,con)

    def obtener_laberinto(self):
        """
        Returns the constructed labyrinth.
        """
        return self._builder.obtener_laberinto()

    def leerArchivo(self, filename):
        """
        Reads a JSON file and parses it into a dictionary.
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            self.dict=data
            return data
        except FileNotFoundError:
            print(f"Error: File not found: {filename}")
            return None
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON format in file: {filename}")
            return None
