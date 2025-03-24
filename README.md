# Laberinto25: diseño UML e implementación en Python
Proyecto de la asignatura Diseño de Software del curso 24-25
El proyecto consiste en diseñar e implementar la lógica de un juego basado en un laberinto
La idea del proyecto está tomada de los ejemplos que aparecen en el libro "Design Patterns: Elements of Reusable Object-Oriented Programming", utilizados para ilustrar los patrones de creación.

Este curso 24-25 utilizaremos los asistentes de AI disponibles. Cada alumno podrá usar el que desee.
En este proyecto se utiliza Cline en VSCode con Geimini

## Factory Method
El primer patrón implementado es el Factory Method. A continuación, se muestra el diagrama de clases.

![laberinto-fm](https://github.com/user-attachments/assets/76cfb4d0-9eb1-4b9e-a36e-1a8ff2089e9a)

## Decorator
Con este patrón podemos agregar responsabilidades nuevas (Bomba) a otros objetos (Pared, Puerta...).
![decorator](https://github.com/user-attachments/assets/5f8839ea-10f1-484e-ae90-15cc09f186e6)

## Strategy
El Strategy encapsula familias de algoritmos como objetos. En nuestra solución lo aplicamos para encapsular el modo (Agresivo, Perezoso) de los bichos.
![strategy](https://github.com/user-attachments/assets/8357957d-3dc6-462b-b8d7-56b5069c74bc)

## Composite
Este patrón se utiliza para representar estructuras recursivas todo-parte. Simplifica a los clientes porque pueden tratar de manera uniforme a compuestos y hojas.
En el caso del proyecto del juego del laberinto, el Composite lo forman ElementoMapa (Component), Contenedor (Composite) y Hoja (Leaf).

![composite](https://github.com/user-attachments/assets/c901618f-64bc-410c-ba11-2d336447ea92)

## Iterator, Singleton y Template Method
### Iterator
Utilizamos un iterador interno que es adecuado para estructuras tipo Composite. El iterador interno se implementa con la operación recorrer(unBloque). El parámetro unBloque es una función anónima.

### Singleton
En esta solución, aplicamos el Singleton a las orientaciones

### Template Method
El método actua de Modo es un Template Method. Las operaciones primitivas son: dormir, caminar y atacar.

<img width="1095" alt="singleton" src="https://github.com/user-attachments/assets/81d5f7a3-6732-401d-938d-c28cd8a4ccff" />

### Builder
Aplicamos el patrón Builder para crear laberintos a partir de un archivo JSON. El participante Director lee el archivo e interpreta el archivo JSON para ir creando cada una de las partes del juego.
![builder](https://github.com/user-attachments/assets/d2d58af6-5c62-4e40-b39c-0fccc41bb9a9)
