# print(2/0)
# raise ZeroDivisionError  # ZeroDivisionError
class MyExeption(Exception):
    def __init__(self, message):
        super().__init__(message)


try:
    x = int(input("Podaj liczbę calkowita"))
    if x < 0:
        print("Liczba powinna byc większa niż zero")
        raise MyExeption("Liczba musi byc dodatnia")
except MyExeption:
    print("Wartośc musi byc większa od zera")
except ValueError:
    print("Błąd wartosci")
