from director import Director
from laberinto_builder import LaberintoBuilder
from laberinto import Laberinto
from habitacion import Habitacion
from puerta import Puerta

# Using the Builder pattern
builder = LaberintoBuilder()
director = Director(builder)
director.construir_laberinto()
laberinto = builder.obtener_laberinto()

if laberinto:
    print("Laberinto construido con el patrón Builder")
else:
    print("No se pudo construir el laberinto")

# Example usage of leerArchivo
filename = "C:\\Users\\jgallud\\CloudStation\\asignaturas\\diseño de sofware\\curso24-25\\laberintos\\lab2Hab.json"

data = director.leerArchivo(filename)
if data:
    print("Data from JSON file:")
    print(data)
else:
    print("Failed to read data from JSON file.")
