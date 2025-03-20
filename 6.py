"""
6. Crea una clase para almacenar duraciones de tiempo (Duration). Los objetos de esta clase son intervalos de tiempo y se crean de la forma:

t1 = Duration(1, 20, 30)  # almacenará 1 hora, 20 minutos y 30 segundos.

t2 = Duration(2, 75, -10)  # almacenará 3 horas, 14 minutos y 50 segundos.

t3 = Duration(t2)  # almacenará las horas, minutos y segundos del objeto t2

Crea los getters y setters mediante propiedades y métodos para:

    Sumar y restar objetos de la clase sobrecargando operadores (el resultado es otro objeto).
    Sumar y restar segundos, minutos o horas (se cambia el objeto actual).
    Devolver una cadena con el tiempo almacenado, de forma que si lo que hay es (10 35 5) la cadena sea 10h 35m 5s.

"""
class Duration:
    def __init__(self, hours=0, minutes=0, seconds=0):
        total_seconds = hours * 3600 + minutes * 60 + seconds
        self.hours = total_seconds // 3600
        self.minutes = (total_seconds % 3600) // 60
        self.seconds = total_seconds % 60

    @property
    def time_str(self):
        return f"{self.hours}h {self.minutes}m {self.seconds}s"

    def __add__(self, other):
        total_seconds = (self.hours + other.hours) * 3600 + \
                        (self.minutes + other.minutes) * 60 + \
                        (self.seconds + other.seconds)
        return Duration(0, 0, total_seconds)

    def __sub__(self, other):
        total_seconds = (self.hours * 3600 + self.minutes * 60 + self.seconds) - \
                        (other.hours * 3600 + other.minutes * 60 + other.seconds)
        return Duration(0, 0, total_seconds)

    def add_time(self, hours=0, minutes=0, seconds=0):
        total_seconds = self.hours * 3600 + self.minutes * 60 + self.seconds + \
                        hours * 3600 + minutes * 60 + seconds
        self.hours = total_seconds // 3600
        self.minutes = (total_seconds % 3600) // 60
        self.seconds = total_seconds % 60

    def __str__(self):
        return self.time_str