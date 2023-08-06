class WeekDayError(Exception):
    pass

class Weeker:
    _valid_days = {"Lun", "Mar", "Mie", "Jue", "Vie", "Sab", "Dom"}

    def __init__(self, day):
        if day not in self._valid_days:
            raise WeekDayError("Invalid day of the week")
        self._day = day

    def __str__(self):
        return self._day

    def add_days(self, n):
        current_index = list(self._valid_days).index(self._day)
        new_index = (current_index + n) % len(self._valid_days)
        self._day = list(self._valid_days)[new_index]

    def subtract_days(self, n):
        current_index = list(self._valid_days).index(self._day)
        new_index = (current_index - n) % len(self._valid_days)
        self._day = list(self._valid_days)[new_index]

# Prueba de la clase Weeker
try:
    day1 = Weeker("Lun")
    print(day1)  # Output: Lun
    day1.add_days(5)
    print(day1)  # Output: Sab
    day1.subtract_days(3)
    print(day1)  # Output: Mie

    day2 = Weeker("Jue")
    print(day2)  # Output: Jue
    day2.add_days(10)
    print(day2)  # Output: Lun

    day3 = Weeker("Foo")  # Debe generar una excepción WeekDayError
except WeekDayError as e:
    print("Error:", e)
