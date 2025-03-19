from creator import Creator, CreatorB
from juego import Juego
import time

#ejemplo de uso
fm = Creator()
juego = Juego()
juego.laberinto = juego.crearLaberinto2HabFM(fm)
hab1=juego.obtenerHabitacion(1)
hab2=juego.obtenerHabitacion(2)
print(hab1.num)
print(hab2.num)

#laberinto con paredes bomba
fmb = CreatorB()
juego.laberinto = juego.crearLaberinto2HabBomba(fmb)
hab1=juego.obtenerHabitacion(1)
hab2=juego.obtenerHabitacion(2)
print(hab1.este.activa)
print(hab2.oeste.activa)

# Crear laberinto de 4 habitaciones
fm = Creator()
juego.laberinto = juego.crearLaberinto4Hab(fm)

# Mostrar el número de cada habitación
for habitacion in juego.laberinto.hijos:
    print(f"Habitación {habitacion.num}")

#mostrar los bichos del juego
for bicho in juego.bichos:
    print(bicho)
    print(f"Bicho con {bicho.vidas} vidas y {bicho.poder} de poder")
    print(f"Posición {bicho.posicion.num}")


# Ejemplo de uso de recorrer con print
print("\nRecorriendo el laberinto e imprimiendo:")
juego.laberinto.recorrer(print)

#def abrirPuertas(obj):
#    if obj.esPuerta():
#        obj.abrir()
juego.abrir_puertas()

juego.cerrar_puertas()

bicho=juego.bichos[0]
juego.lanzarBicho(bicho)
time.sleep(3)
bicho.vidas=0
