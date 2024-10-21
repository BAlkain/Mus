# MUS

Este proyecto es un simulador del juego de cartas **Mus** escrito en Python, desarrollado por **Beñat Alkain Epelde**. El juego está diseñado para ser jugado por cuatro jugadores, divididos en dos equipos, siguiendo las reglas tradicionales del Mus, con algunas simplificaciones.

## Descripción General

El programa permite a los jugadores jugar al Mus utilizando una implementación de la baraja española. Los jugadores realizan apuestas y juegan rondas de comparaciones (Grande, Chica, Parejas y Juego) hasta que uno de los equipos alcanza 40 puntos para ganar la partida.

## Características

- **Baraja Española**: El juego utiliza una baraja española de 40 cartas (Oros, Copas, Espadas y Bastos).
- **Jugadores y Equipos**: Hay cuatro jugadores divididos en dos equipos.
- **Rondas de Comparación**: Se realizan comparaciones en Grande, Chica, Parejas y Juego para determinar al ganador de cada ronda.
- **Apuestas**: Los jugadores pueden realizar apuestas de "Envido" (2 puntos), "Paso" o "Órdago" (apuesta total para ganar la partida).

## Limitaciones

- Solo se permiten **envidos** de 2 puntos.
- Siempre empieza **el mismo equipo** en cada ronda, ya que no se manejan turnos de manera dinámica.

## Clases Principales

El código está organizado en varias clases para representar los diferentes componentes del juego:

- **Carta**: Representa una carta individual de la baraja, con un valor y un palo.
- **Baraja**: Contiene todas las cartas del juego y proporciona funciones para mezclar y repartir las cartas.
- **Jugador**: Representa a cada jugador y gestiona su mano de cartas.
- **ComparacionBase**: Clase abstracta utilizada para las comparaciones de Grande, Chica, Parejas y Juego.
- **Grandes, Chicas, Parejas, Juego**: Clases que heredan de `ComparacionBase` y realizan comparaciones específicas para cada categoría del Mus.
- **JuegoMus**: Controla el flujo general del juego, incluyendo la gestión de las rondas, apuestas y puntuaciones.

## Ejecución

Para ejecutar el juego, sigue los siguientes pasos:

1. Asegúrate de tener Python 3.x instalado en tu sistema.
2. Descarga el archivo `.py` con el código.
3. Abre una terminal o línea de comandos, navega hasta el directorio donde se encuentra el archivo y ejecuta el siguiente comando:

   ```bash
   python nombre_del_archivo.py
   ```

   Reemplaza `nombre_del_archivo.py` con el nombre real del archivo.

4. Sigue las instrucciones en pantalla para interactuar con el juego. Se te pedirá que tomes decisiones como aceptar o rechazar apuestas.

## Reglas del Juego

- **Mus**: Todos los jugadores deben estar de acuerdo para pedir mus (cambiar las cartas), si algún jugador no quiere, se empieza la ronda con las cartas actuales.
- **Comparaciones**:
  - **Grandes**: Se comparan las cartas de mayor a menor.
  - **Chicas**: Se comparan las cartas de menor a mayor.
  - **Parejas**: Se determina quién tiene pares, medias o duples.
  - **Juego**: Se calcula el valor total de las cartas para determinar si hay juego o punto.
- **Apuestas**: Se pueden hacer apuestas de "Envido" (2 puntos) o "Órdago" (apuesta total). Si un equipo rechaza una apuesta, el otro equipo gana 1 punto.

## Autor

- **Beñat Alkain Epelde**

## Licencia

Este proyecto no especifica una licencia. Para usos o modificaciones, por favor, contacta al autor.

---

¡Disfruta del juego y que gane el mejor equipo!

