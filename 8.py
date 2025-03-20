"""
8. Muestra un menú con las siguientes opciones:

    Introducir (por teclado) una fecha pidiendo por teclado año, mes y día en formato dd/mm/aaaa. Si no se introduce correctamente se devuelve un mensaje de error. Usa una función booleana para validar la fecha.
    Añadir días a la fecha. Pide un número de días para sumar a la fecha introducida previamente y actualiza su valor. Si el número es negativo restará los días. Esta opción sólo podrá realizarse si hay una fecha introducida (se ha ejecutado la opción anterior), si no la hay mostrará un mensaje de error. 
    Añadir meses a la fecha. El mismo procedimiento que la opción anterior.
    Añadir años a la fecha. El mismo procedimiento que la opción 2.
    Comparar la fecha introducida con otra. Pide una fecha al usuario en formato dd/mm/aaaa (válida, si no lo es da error) y la comparará con la que tenemos guardada, posteriormente mostrará si esta fecha es anterior, igual o posterior a la que tenemos almacenada y el número de días comprendido entre las dos fechas.
    Mostrar la fecha en formato largo (ejemplo: "lunes, 1 de febrero de 2021").
    Terminar.

"""
from datetime import date, timedelta

class Menu:
    def __init__(self):
        self.options = []
        self.stored_date = None

    def add_option(self, description, action):
        self.options.append((description, action))

    def execute_option(self, option_number):
        if 0 < option_number <= len(self.options):
            self.options[option_number - 1][1]()
        else:
            print("Opción inválida")

    def display_menu(self):
        print("Menú:")
        for i, (description, _) in enumerate(self.options, start=1):
            print(f"{i}. {description}")

def validate_date(input_date):
    try:
        day, month, year = map(int, input_date.split("/"))
        return date(year, month, day)
    except ValueError:
        print("Fecha inválida. Inténtalo nuevamente.")
        return None

def add_days(stored_date):
    if stored_date is None:
        print("No hay ninguna fecha almacenada.")
        return
    days = int(input("Introduce el número de días a añadir: "))
    stored_date += timedelta(days=days)
    print("Fecha actualizada:", stored_date)

menu = Menu()
menu.add_option("Introducir una fecha", lambda: validate_date(input("Introduce una fecha (dd/mm/aaaa): ")))
menu.add_option("Añadir días", lambda: add_days(menu.stored_date))
menu.add_option("Terminar", lambda: print("¡Hasta luego!") or exit())

menu.display_menu()
option = int(input("Escoge una opción: "))
menu.execute_option(option)