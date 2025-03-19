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
        """
        Constructs the labyrinth step by step.
        """
        self._builder.construir_laberinto()
        # Add more steps here as needed, e.g., adding rooms and doors

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
