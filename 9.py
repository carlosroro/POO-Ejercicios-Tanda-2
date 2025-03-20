"""
9. Nos hemos enterado que la clase datetime.date ha sido comprometida y tenemos que crear una clase nueva para almacenar fechas locales (Date), en este caso la clase será mutable (los objetos pueden cambiar el día, mes o año). Los objetos de la clase Fecha son fechas de tiempo y se crean de la forma:

f1 = Date(1, 10, 2020)  # almacena el 1 de Octubre de 2020
f2 = Date(f1)  # almacena una copia de la fecha almacenada en f1

Para simplificar consideraremos que las fechas son todas a partir del 1 de enero del año 1.

Si al constructor se le pasan valores incorrectos lanzaremos la excepción ValueError.

Crea métodos para:

    Sumar y restar días a la fecha. 
    Restar fechas. Devuelve el número de días comprendidos entre ambas.
    Comparar la fecha almacenada con otra.
    Saber si el año de la fecha almacenada es bisiesto.
    Obtener el día de la semana de una fecha concreta.
    El método __str__() devuelve una cadena con el formato "<día del mes> de <nombre del mes> de <año>".

"""
class Date:
    def __init__(self, day, month, year):
        if not (1 <= day <= 31 and 1 <= month <= 12 and year > 0):
            raise ValueError("Fecha inválida")
        self.day = day
        self.month = month
        self.year = year

    def add_days(self, days):
        self.day += days
        return self

    def days_between(self, other):
        d1 = self.year * 365 + self.month * 30 + self.day
        d2 = other.year * 365 + other.month * 30 + other.day
        return abs(d1 - d2)

    def __str__(self):
        months = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
                  "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
        return f"{self.day} de {months[self.month - 1]} de {self.year}"