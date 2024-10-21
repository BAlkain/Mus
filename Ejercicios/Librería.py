# Excepción personalizada para año de publicación inválido
class ExcepcionAnioInvalido(Exception):
    def __init__(self, mensaje="El año de publicación no puede ser menor a 1440."):
        super().__init__(mensaje)

# Clase Libro
class Libro:
    def __init__(self, titulo, autor, anio_publicacion, copias_disponibles=1):
        self._titulo = titulo
        self._autor = autor
        self.anio_publicacion = anio_publicacion  # Setter llamado para validación
        self.copias_disponibles = copias_disponibles  # Setter con assert

    # Getters
    @property
    def titulo(self):
        return self._titulo

    @property
    def autor(self):
        return self._autor

    @property
    def anio_publicacion(self):
        return self._anio_publicacion

    @property
    def copias_disponibles(self):
        return self._copias_disponibles

    # Setters
    @anio_publicacion.setter
    def anio_publicacion(self, anio):
        if anio < 1440:
            raise ExcepcionAnioInvalido()
        self._anio_publicacion = anio

    @copias_disponibles.setter
    def copias_disponibles(self, copias):
        assert copias >= 0, "El número de copias disponibles no puede ser negativo."
        self._copias_disponibles = copias

# Clase LibroPrestado (hereda de Libro)
class LibroPrestado(Libro):
    def __init__(self, titulo, autor, anio_publicacion, copias_disponibles=1):
        super().__init__(titulo, autor, anio_publicacion, copias_disponibles)
        self.prestado = False

    def prestar_libro(self):
        if self.prestado:
            raise Exception("El libro ya está prestado.")
        if self.copias_disponibles <= 0:
            raise Exception("No hay copias disponibles para prestar.")
        self.prestado = True
        self.copias_disponibles -= 1

    def devolver_libro(self):
        if not self.prestado:
            raise Exception("El libro no estaba prestado.")
        self.prestado = False
        self.copias_disponibles += 1

# Clase Libreria
class Libreria:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, *args, **kwargs):
        libro = Libro(*args, **kwargs)
        self.libros.append(libro)

    def buscar_libro_por_titulo(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None

    def prestar_libro(self, titulo):
        libro = self.buscar_libro_por_titulo(titulo)
        if not libro:
            raise Exception("El libro no se encuentra en la librería.")
        if isinstance(libro, LibroPrestado):
            libro.prestar_libro()
        else:
            raise Exception("El libro no es prestable.")


# Ejemplo de uso del sistema de gestión de librería

# Crear una instancia de la librería
mi_libreria = Libreria()

# Agregar algunos libros a la librería
mi_libreria.agregar_libro("Cien Años de Soledad", "Gabriel García Márquez", 1967, copias_disponibles=5)
mi_libreria.agregar_libro("Don Quijote", "Miguel de Cervantes", 1605, copias_disponibles=3)

# Agregar un libro prestable
libro_prestable = LibroPrestado("El Principito", "Antoine de Saint-Exupéry", 1943, copias_disponibles=2)
mi_libreria.libros.append(libro_prestable)

# Buscar un libro en la librería
libro = mi_libreria.buscar_libro_por_titulo("Cien Años de Soledad")
if libro:
    print(f"Encontrado el libro: {libro.titulo}, de {libro.autor}.")

# Prestar un libro
try:
    print("\nIntentando prestar 'El Principito'...")
    libro_prestable.prestar_libro()
    print(f"Libro prestado con éxito. Copias disponibles: {libro_prestable.copias_disponibles}.")
except Exception as e:
    print(f"Error al prestar el libro: {e}")

# Intentar prestar el mismo libro nuevamente (debería lanzar una excepción)
try:
    print("\nIntentando prestar 'El Principito' nuevamente...")
    libro_prestable.prestar_libro()  # Esto debería fallar
except Exception as e:
    print(f"Error al prestar el libro: {e}")

# Devolver el libro
try:
    print("\nDevolviendo 'El Principito'...")
    libro_prestable.devolver_libro()
    print(f"Libro devuelto con éxito. Copias disponibles: {libro_prestable.copias_disponibles}.")
except Exception as e:
    print(f"Error al devolver el libro: {e}")

# Intentar devolver el mismo libro otra vez (debería lanzar una excepción)
try:
    print("\nIntentando devolver 'El Principito' nuevamente...")
    libro_prestable.devolver_libro()  # Esto debería fallar
except Exception as e:
    print(f"Error al devolver el libro: {e}")
