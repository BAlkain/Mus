#############################################################################
# MUS
# #(8 reyes, 40 puntos)
# Beñat Alkain Epelde
#############################################################################
#
# Limitaciones:
# - Solo se pueden realizar envidos de 2 puntos
# - No se tienen en cuenta los turnos. Siempre empieza "el mismo equipo".

import random
from collections import Counter

#############################################################################

# Clase Carta
# Descripción: Representa una carta individual de la baraja española, con un valor y un palo (Oros, Copas, Espadas, Bastos).
# Atributos:
# valor: El valor de la carta (1, 2, 3, 4, 5, 6, 7, 10, 11, 12).
# palo: El palo de la carta (Oros, Copas, Espadas, Bastos).
# Métodos:
# valor_grande(): Devuelve el valor para la comparación en Grande.
# valor_chica(): Devuelve el valor para la comparación en Chica.
# valor_pareja(): Devuelve el valor para la comparación en Parejas.
# valor_juego(): Devuelve el valor para la comparación en Juego.

class Carta:
    def __init__(self, valor, palo):
        self._valor = valor
        self._palo = palo

    def __repr__(self):
        return f"{self.valor} de {self.palo}"

    @property
    def valor(self):
        return self._valor

    @property
    def palo(self):
        return self._palo

    def valor_grande(self):
        if self.valor == 3:
            return 12
        elif self.valor == 2:
            return 1
        return self.valor

    def valor_chica(self):
        if self.valor == 3:
            return 12
        elif self.valor == 2:
            return 1
        return 14 - self.valor

    def valor_pareja(self):
        if self.valor == 3:
            return 12
        elif self.valor == 2:
            return 1
        return self.valor

    def valor_juego(self):
        if self.valor in [3, 10, 11, 12]:
            return 10
        elif self.valor == 2:
            return 1
        return self.valor

#############################################################################

# Clase Baraja
# Descripción: Representa una baraja de cartas españolas.
# Atributos:
# cartas: Una lista de objetos Carta que representa todas las cartas de la baraja.
# Métodos:
# crear_baraja(): Genera las cartas de la baraja.
# mezclar(): Mezcla las cartas.
# repartir(): Reparte cartas a los jugadores, eliminando cartas de la baraja.

class Baraja:
    def __init__(self):
        self._cartas = []
        print("Creando baraja...")
        self.crear_baraja()
        print(f"Baraja creada con {len(self.cartas)} cartas.")

    @property
    def cartas(self):
        return self._cartas

    def crear_baraja(self):
        palos = ['Oros', 'Copas', 'Espadas', 'Bastos']
        valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
        self._cartas = [Carta(valor, palo) for palo in palos for valor in valores]

    def mezclar(self):
        print("Mezclando la baraja...")
        random.shuffle(self.cartas)
        print("Baraja mezclada.")

    def repartir(self, jugadores, num_cartas=4):
        print(f"Repartiendo {num_cartas} cartas a cada jugador...")
        for _ in range(num_cartas):
            for jugador in jugadores:
                carta_repartida = self.cartas.pop()
                jugador.recibir_carta(carta_repartida)
                print(f"{jugador.nombre} recibe {carta_repartida}")
        print("Cartas repartidas a todos los jugadores.")

#############################################################################

# Clase Jugador
# Descripción: Representa un jugador en el juego.
# Atributos:
# nombre: El nombre del jugador.
# mano: La lista de cartas que el jugador tiene en su mano.
# Métodos:
# recibir_carta(): Añade una carta a la mano del jugador.
# mostrar_mano(): Muestra las cartas que el jugador tiene en su mano.
# tiene_parejas(): Verifica si el jugador tiene al menos una pareja (dos cartas iguales).
# valor_mejor_pareja(): Devuelve el valor de la mejor pareja.
# valor_juego(): Calcula el valor total de las cartas del jugador para la comparación de Juego.

class Jugador:
    def __init__(self, nombre):
        self._nombre = nombre
        self._mano = []
        print(f"Creando jugador: {self._nombre}")

    @property
    def nombre(self):
        return self._nombre

    @property
    def mano(self):
        return self._mano

    def recibir_carta(self, carta):
        self._mano.append(carta)

    def mostrar_mano(self):
        return f"{self.nombre} tiene {', '.join(map(str, self._mano))}"

    def limpiar_mano(self):
        self._mano = []

    def tiene_parejas(self):
        valores = [carta.valor_pareja() for carta in self._mano]
        return any(count >= 2 for count in Counter(valores).values())

    def valor_mejor_pareja(self):
        valores = [carta.valor_pareja() for carta in self._mano]
        parejas = [valor for valor, count in Counter(valores).items() if count >= 2]
        return max(parejas) if parejas else 0

    def valor_juego(self):
        return sum(carta.valor_juego() for carta in self._mano)

#############################################################################

# Clase ComparacionBase
# Descripción: Clase base para realizar comparaciones entre jugadores en diferentes categorías (Grande, Chica, Parejas, Juego). Esta clase es abstracta y debe ser extendida por clases específicas.
# Atributos:
# jugadores: La lista de jugadores que participan en la comparación.
# nombre_comparacion: El nombre de la comparación (por ejemplo, "Grandes").
# ganador: Almacena el ganador de la comparación.
# Métodos:
# comparar(): Realiza la comparación entre las cartas de los jugadores, buscando el mayor valor.
# criterio_ordenacion(): Metodo abstracto que debe implementarse en las clases hijas para definir cómo se ordenan las cartas.

class ComparacionBase:
    def __init__(self, jugadores, nombre_comparacion):
        self.jugadores = jugadores
        self.nombre_comparacion = nombre_comparacion
        self.ganador = None  # Atributo para almacenar el ganador

    def comparar(self):
        print(f"\n--- {self.nombre_comparacion} ---")
        manos_ordenadas = [sorted(jugador.mano, key=self.criterio_ordenacion(), reverse=True) for jugador in
                           self.jugadores]

        ganador = None
        for i in range(4):  # Comparar las 4 cartas
            max_valor = max(self.criterio_ordenacion()(mano[i]) for mano in manos_ordenadas)
            jugadores_max = [j for j, mano in enumerate(manos_ordenadas) if
                             self.criterio_ordenacion()(mano[i]) == max_valor]

            if len(jugadores_max) == 1:
                ganador = self.jugadores[jugadores_max[0]]
                break

        if ganador:
            self.ganador = ganador #Almacenar ganador
            print(f"{ganador.nombre} gana en {self.nombre_comparacion.lower()} con {ganador.mostrar_mano()}")
        else:
            print(f"Empate en {self.nombre_comparacion.lower()}")

    def criterio_ordenacion(self):
        raise NotImplementedError("Debe implementarse en las clases hijas")

#############################################################################

# Clases que heredan de ComparacionBase:
# Grandes:
# Compara los jugadores según los valores de Grande usando el metodo valor_grande() de las cartas.
# Parejas:
# Compara las manos de los jugadores para determinar si tienen pares, medias o duples.
# Métodos adicionales:
# revelar_parejas(): Verifica qué jugadores tienen parejas antes de las apuestas.
# comparar(): Da prioridad a los jugadores con duples (dos pares) sobre aquellos con medias (tres cartas iguales) o pares (dos cartas iguales).
# obtener_prioridad_parejas(): Devuelve un número que indica la prioridad de la combinación del jugador (1 para pares, 2 para medias, 3 para duples).
# print_tipo_pareja(): Imprime el tipo de pareja que tiene el jugador y cuántos puntos obtiene.
# Juego:
# Compara las manos de los jugadores según el valor de Juego (si tienen 31, más de 30, o si no tienen juego).
# Métodos adicionales:
# valor_juego_ajustado(): Ajusta los valores del juego para la comparación (por ejemplo, 31 es la mejor jugada).

class Grandes(ComparacionBase):
    def __init__(self, jugadores):
        super().__init__(jugadores, "Grandes")

    def criterio_ordenacion(self):
        return lambda c: c.valor_grande()
class Chicas(ComparacionBase):
    def __init__(self, jugadores):
        super().__init__(jugadores, "Chicas")

    def criterio_ordenacion(self):
        return lambda c: c.valor_chica()
class Parejas(ComparacionBase):
    def __init__(self, jugadores):
        super().__init__(jugadores, "Parejas")
        self.jugadores_con_parejas = []  # Almacenar los jugadores que tienen parejas

    def revelar_parejas(self):
        print("\n--- Parejas ---")

        # Los jugadores dicen si tienen parejas
        self.jugadores_con_parejas = []
        for jugador in self.jugadores:
            tiene_pareja = jugador.tiene_parejas()
            print(f"{jugador.nombre}: {'Sí' if tiene_pareja else 'No'}")
            if tiene_pareja:
                self.jugadores_con_parejas.append(jugador)

        if not self.jugadores_con_parejas:
            print("Nadie tiene parejas.")
            self.ganador = None
            return False  # Si nadie tiene parejas, no continuamos con las apuestas
        return True  # Continuar con las apuestas

    def comparar(self):
        # Determinar el ganador después de las apuestas, dando prioridad a duples > medias > pares
        if self.jugadores_con_parejas:
            ganador = max(self.jugadores_con_parejas, key=lambda j: (self.obtener_prioridad_parejas(j), j.valor_mejor_pareja()))
            self.ganador = ganador
            self.print_tipo_pareja(ganador)  # Imprimir el tipo de pareja que tiene el ganador
        else:
            self.ganador = None

    def obtener_prioridad_parejas(self, jugador): #Determina la prioridad de la combinación que tiene el jugador
        valores = [carta.valor_pareja() for carta in jugador.mano]
        conteo = Counter(valores)
        pares = sum(1 for count in conteo.values() if count == 2) # Contar cuántos pares y cuántos tríos hay
        medias = sum(1 for count in conteo.values() if count == 3)

        if pares == 2: # Si hay dos pares distintos, es Duples
            return 3  # Duples (dos pares)
        # Si hay un trío, es Medias
        elif medias == 1:
            return 2  # Medias (tres cartas iguales)
        # Si hay un solo par, es Par
        elif pares == 1:
            return 1  # Pares (dos cartas iguales)
        else:
            return 0  # No hay parejas, medias ni duples

    def print_tipo_pareja(self, jugador): # Imprimir el tipo de pareja que tiene el jugador (pares, medias o duples) y los puntos que se lleva
        prioridad = self.obtener_prioridad_parejas(jugador)
        if prioridad == 3:
            print(f"{jugador.nombre} tiene duples (dos pares) y gana 3 puntos.")
        elif prioridad == 2:
            print(f"{jugador.nombre} tiene medias (tres cartas iguales) y gana 2 puntos.")
        else:
            print(f"{jugador.nombre} tiene pares (solo dos cartas iguales) y gana 1 punto.")

    def criterio_ordenacion(self):
        return lambda c: c.valor_pareja()
class Juego(ComparacionBase):
    def __init__(self, jugadores):
        super().__init__(jugadores, "Juego")

    def comparar(self):
        print("\n--- Juego ---")

        jugadores_con_juego = []
        jugadores_sin_juego = []

        for jugador in self.jugadores:
            valor = jugador.valor_juego()
            print(f"{jugador.nombre}: {valor} ({', '.join(str(c.valor) for c in jugador.mano)})")
            if valor >= 31:
                jugadores_con_juego.append(jugador)
            else:
                jugadores_sin_juego.append(jugador)

        if jugadores_con_juego:
            ganador = max(jugadores_con_juego, key=lambda j: self.valor_juego_ajustado(j.valor_juego()))
            self.ganador = ganador
            print(f"{ganador.nombre} gana en juego con {ganador.valor_juego()} ({ganador.mostrar_mano()})")
        elif jugadores_sin_juego:
            ganador = max(jugadores_sin_juego, key=lambda j: j.valor_juego())
            self.ganador = ganador
            print(f"{ganador.nombre} gana en punto con {ganador.valor_juego()} ({ganador.mostrar_mano()})")
        else:
            print("Empate en juego")
            self.ganador = None

    def valor_juego_ajustado(self, valor):
        if valor == 31: #Mejor jugada de juego
            return 8
        elif valor == 32:
            return 7
        elif valor >= 40:
            return 6
        elif 33 <= valor <= 37:
            return 37 - valor + 1
        else:
            return 0 #Es necesario?

    def criterio_ordenacion(self):
        return lambda j: self.valor_juego_ajustado(j.valor_juego())

#############################################################################

# Clase JuegoMus
# Descripción: Controla el flujo completo del juego de Mus, incluyendo la baraja, los jugadores, y las reglas del juego.
# Atributos:
# baraja: Un objeto de la clase Baraja, que contiene las cartas.
# jugadores: Una lista de objetos Jugador que participan en el juego.
# equipos: Una lista de equipos, donde cada equipo tiene jugadores y una puntuación global.
# Métodos:
# iniciar_juego(): Inicia el juego, gestionando las rondas, el reparto de cartas y las comparaciones.
# realizar_comparacion(): Realiza una comparación (por ejemplo, Grande, Chica, Parejas, Juego), permitiendo apuestas y otorgando puntos según el resultado.
# otorgar_puntos_automaticos(): Otorga puntos automáticamente al ganador de la comparación si no hay apuestas.
# puntos_por_comparacion(): Calcula cuántos puntos obtiene el ganador según la categoría (1 punto para Grande y Chica, 1-3 puntos para Parejas según la combinación, 2-3 puntos para Juego).
# repartir_cartas(): Mezcla la baraja y reparte cartas a los jugadores al inicio de cada ronda.
# mus(): Verifica si los jugadores quieren pedir Mus (cambiar cartas).
# realizar_apuestas(): Gestiona las apuestas entre los equipos, permitiendo envido, paso o órdago.

class JuegoMus:
    def __init__(self):
        print("Iniciando juego de Mus...")
        self._baraja = Baraja()
        self._jugadores = [Jugador(nombre) for nombre in ['Alkain', 'Wili', 'Telmo', 'Txerriya']]
        self._equipos = [
            {'nombre': 'Equipo 1 (Beñat, Wili)', 'jugadores': [self._jugadores[0], self._jugadores[1]], 'puntos_globales': 0},
            {'nombre': 'Equipo 2 (Telmo, Txerriya)', 'jugadores': [self._jugadores[2], self._jugadores[3]], 'puntos_globales': 0}
        ]

    @property
    def baraja(self):
        return self._baraja

    @property
    def jugadores(self):
        return self._jugadores

    @property
    def equipos(self):
        return self._equipos

    def otorgar_puntos_automaticos(self, comparacion): # Da puntos automáticamente según la categoría ganada.
        ganador = comparacion.ganador
        if ganador:
            equipo_ganador = next(e for e in self.equipos if ganador in e['jugadores'])
            puntos = self.puntos_por_comparacion(comparacion)
            equipo_ganador['puntos_globales'] += puntos
            print(
                f"{equipo_ganador['nombre']} gana automáticamente {puntos} puntos en {comparacion.nombre_comparacion.lower()}.")

    def puntos_por_comparacion(self, comparacion): #Determinar cuántos puntos se otorgan en función de la comparación ganada.
        if isinstance(comparacion, Grandes) or isinstance(comparacion, Chicas):
            return 1  # Grande y Chica otorgan 1 punto
        elif isinstance(comparacion, Parejas): # Verificar tipo de pareja (pares, medias o duples)
            valores = [carta.valor_pareja() for carta in comparacion.ganador.mano]
            conteo = Counter(valores)

            if 4 in conteo.values():
                return 3  # Duples, 3 puntos
            elif 3 in conteo.values():
                return 2  # Medias, 2 puntos
            else:
                return 1  # Pares, 1 punto
        elif isinstance(comparacion, Juego): # Juego de 31 otorga 3 puntos, los demás juegos 2, sin juego otorga 1
            for jugador in comparacion.jugadores:
                if jugador.valor_juego() == 31:
                    return 3
            return 2 if comparacion.ganador else 1  # Juego otorga 2 puntos, no juego 1
        return 1  # Por defecto

    def iniciar_juego(self):
        print("\n--- Comienza el juego ---")

        while True:
            self.repartir_cartas() # Repartir cartas al inicio de cada ronda

            while self.mus(): # El juego sigue hasta que alguien no quiera mus
                print("\nTodos quieren mus. Volviendo a repartir...")
                self.repartir_cartas()

            print("\n¡Comienza la partida!")
            for jugador in self._jugadores:
                print(jugador.mostrar_mano())

            # Realizamos las comparaciones, repitiendo el ciclo de apuestas hasta que alguien llegue a 40 puntos
            if not self.realizar_comparacion(Grandes(self._jugadores)):
                return  # Termina si se gana por órdago
            if not self.realizar_comparacion(Chicas(self._jugadores)):
                return  # Termina si se gana por órdago
            if not self.realizar_comparacion(Parejas(self._jugadores)):
                return  # Termina si se gana por órdago
            if not self.realizar_comparacion(Juego(self._jugadores)):
                return  # Termina si se gana por órdago

            for equipo in self._equipos: # Después de cada ronda, verificar si algún equipo ha llegado a 40 puntos
                if equipo['puntos_globales'] >= 40:
                    print(f"\n¡¡¡{equipo['nombre']} HA GANADO LA PARTIDA CON {equipo['puntos_globales']} PUNTOS!!!")
                    return

    def repartir_cartas(self):
        for jugador in self._jugadores:
            jugador.limpiar_mano()
        self._baraja = Baraja()
        self._baraja.mezclar()
        self._baraja.repartir(self._jugadores)

    def mus(self):
        print("\n--- ¿Mus? ---")
        for jugador in self._jugadores:
            quiere_mus = input(f"{jugador.nombre}, ¿quieres mus? (Sí/No): ").strip().lower()
            if quiere_mus != 'sí' and quiere_mus != 'si':
                print(f"{jugador.nombre} no quiere mus. Se mantienen las cartas.")
                return False
        return True

    def realizar_comparacion(self, comparacion):
        # Para parejas, primero revelamos quién tiene pareja antes de las apuestas
        if isinstance(comparacion, Parejas):
            if not comparacion.revelar_parejas():  # Si no hay jugadores con pareja, no continuamos
                self.imprimir_puntuaciones()
                return True  # Continuar sin apuestas
        equipo_apostador, puntos_apostados, apuesta_aceptada = self.realizar_apuestas() # Realizamos las apuestas después de revelar las parejas
        comparacion.comparar() # Después de las apuestas, comparamos para encontrar al ganador
        ganador = comparacion.ganador  # Identificar el ganador tras la comparación
        puntos_categoria = self.puntos_por_comparacion(comparacion)  # Puntos automáticos por la categoría ganada

        if not apuesta_aceptada or puntos_apostados == 0: # Si no hay apuestas o los puntos apostados son 0, otorgar solo los puntos automáticos
            self.otorgar_puntos_automaticos(comparacion)
        else:
            if ganador: # Si hay apuestas, otorgamos puntos basados apuesta + puntos de la categoría
                equipo_ganador = next(e for e in self.equipos if ganador in e['jugadores'])

                if puntos_apostados == 40:  # Si fue un órdago aceptado
                    equipo_ganador['puntos_globales'] = 40  # Ganador del órdago se lleva toda la partida
                    print(f"\n¡{equipo_ganador['nombre']} GANA EL ÓRDAGO!")
                    self.imprimir_puntuaciones()
                    return False  # Termina el juego
                else:
                    total_puntos = puntos_apostados + puntos_categoria # Sumar tanto los puntos apostados como los puntos de la categoría ganada
                    equipo_ganador['puntos_globales'] += total_puntos
                    print(
                        f"{equipo_ganador['nombre']} gana la apuesta y se lleva {puntos_apostados} puntos más {puntos_categoria} por {comparacion.nombre_comparacion.lower()}. Total: {total_puntos} puntos.")
            else:
                if puntos_apostados == 40:  # Si es un órdago y hay empate
                    print("\nEmpate en el órdago, pero el juego debe finalizar.")
                    self.imprimir_puntuaciones()
                    return False  # Termina el juego
                else:
                    print("Empate, no se asignan puntos.")
        self.imprimir_puntuaciones() # Imprimir las puntuaciones actualizadas
        return True  # El juego sigue

    def imprimir_puntuaciones(self):
        print("\n--- Puntuaciones Totales ---")
        for equipo in self.equipos:
            print(f"{equipo['nombre']}: {equipo['puntos_globales']} puntos")

    def realizar_apuestas(self):
        print("\n--- Apuestas ---")

        while True:
            try: # Preguntar al equipo 1 primero
                decision_equipo1 = input(f"{self.equipos[0]['nombre']}, ¿Envido, Paso o Órdago? ").strip().lower()
                if decision_equipo1 not in ['envido', 'paso', 'órdago']:
                    raise ValueError  # Lanzamos un error si no se ha escrito bien el prompt
                break
            except ValueError:
                print("Introduce alguna de las jugadas posibles: Paso, Envido o Órdago")

        puntos_apostados = 2 if decision_equipo1 == 'envido' else 0
        if decision_equipo1 == 'órdago':
            puntos_apostados = 40  # Apuesta total de 40 puntos en órdago

        if decision_equipo1 == 'paso': # Si el equipo 1 dice "Paso", se le pregunta al equipo 2
            while True:
                try:
                    decision_equipo2 = input(f"{self.equipos[1]['nombre']}, ¿Envido, Paso o Órdago? ").strip().lower()
                    if decision_equipo2 not in ['envido', 'paso', 'órdago']:
                        raise ValueError  # Lanzamos un error si la jugada no es válida
                    break
                except ValueError:
                    print("Introduce alguna de las jugadas posibles: Paso, Envido o Órdago")

            puntos_apostados = 2 if decision_equipo2 == 'envido' else 0
            if decision_equipo2 == 'órdago':
                puntos_apostados = 40  # Apuesta total de 40 puntos en órdago

            # Si el equipo 2 también dice "Paso", no hay apuestas
            if decision_equipo2 == 'paso':
                print("Ambos equipos han pasado. No hay apuestas en esta ronda.")
                return None, 0, True  # No hay apuestas, continúa sin apuestas

            # Si el equipo 2 hace una apuesta (Envido u Órdago), se le pregunta al equipo 1 si acepta
            while True:
                try:
                    decision_equipo1_aceptar = input(
                        f"{self.equipos[0]['nombre']}, ¿Aceptas la apuesta de {self.equipos[1]['nombre']}? (Sí/No): ").strip().lower()
                    if decision_equipo1_aceptar not in ['sí', 'no']:
                        raise ValueError  # Lanzamos un error si la respuesta no es válida
                    break
                except ValueError:
                    print("Introduce una respuesta válida: Sí o No")

            if decision_equipo1_aceptar == 'no':
                # Si equipo 1 no acepta, equipo 2 gana automáticamente 1 punto global
                self.equipos[1]['puntos_globales'] += 1
                print(
                    f"{self.equipos[0]['nombre']} no acepta la apuesta. {self.equipos[1]['nombre']} gana 1 punto global.")
                return self.equipos[1], 1, False  # El tercer valor indica que la apuesta no fue aceptada
            # Si el equipo 1 acepta la apuesta del equipo 2, se juega con los puntos apostados
            return self.equipos[1], puntos_apostados, True  # Apuesta aceptada por el equipo 1
        # Si el equipo 1 hace una apuesta (Envido u Órdago) y no pasa, el flujo sigue como antes
        if puntos_apostados > 0:
            while True:
                try:
                    decision_equipo2 = input(
                        f"{self.equipos[1]['nombre']}, ¿Aceptas la apuesta de {self.equipos[0]['nombre']}? (Sí/No): ").strip().lower()
                    if decision_equipo2 not in ['sí', 'no']:
                        raise ValueError  # Lanzamos un error si la respuesta no es válida
                    break
                except ValueError:
                    print("Introduce una respuesta válida: Sí o No")

            if decision_equipo2 == 'no':
                # Si equipo 2 no acepta, equipo 1 gana automáticamente 1 punto global
                self.equipos[0]['puntos_globales'] += 1
                print(
                    f"{self.equipos[1]['nombre']} no acepta la apuesta. {self.equipos[0]['nombre']} gana 1 punto global.")
                return self.equipos[0], 1, False  # El tercer valor indica que la apuesta no fue aceptada
        # Si el equipo 2 acepta, la apuesta sigue con los puntos apostados
        return self.equipos[0], puntos_apostados, True  # Apuesta aceptada por el equipo 2

#############################################################################

# Ejecución
juego = JuegoMus()
juego.iniciar_juego()
