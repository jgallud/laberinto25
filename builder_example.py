from director import Director
from laberinto_builder import LaberintoBuilder
from laberinto import Laberinto
from habitacion import Habitacion
from puerta import Puerta

director = Director()

filename = "-ruta-del-directorio-\\laberintos\\lab2Hab.json"

data = director.leerArchivo(filename)
if data:
    print("Data from JSON file:")
    print(data)
else:
    print("Failed to read data from JSON file.")

juego = director.procesar(filename)