# funkcje - wydzielony fragment kodu
# funkcje mozna wywołac w dowolnym momencie
# funkcja musi byc najpierw zdeklarowana zanim zostanie uzyta
# w miejscu deklaracji funkcja nie jest uruchamiana
# aby wykonac funkcje trzeba ja wywołac

a = 8
b = 9


# deklaracja funkcji
def dodaj():
    print(a + b)


def dodaj2(a, b):  # funkcja ma 2 argumenty, a i b sa o zasiegu lokalnym, argumenty obowiazkowe
    print(a + b)


# podpowiedzi typów to nie weryfikacja typów (walidacja)
def odejmij(a: int, b: int, c=0):  # c ma wartośc domyślną, jest opcjonalny
    print(a - b - c)


def mnozenie(a, b):
    return a * b


def mnozenie2(a, b):
    return a, b, a * b


# wykonanie funkcji
dodaj()  # 17
dodaj2(2, 3)  # 5
# dodaj2()  # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
# symulacja przeciązania liczby argumentów funkcji za pomocą wartości domyślnej argumentu c
odejmij(1, 2, 3)  # przekazanie argumentów po pozycji
odejmij(1, 2)
# odejmij("a",2)  # TypeError: unsupported operand type(s) for -: 'str' and 'int'
odejmij(b=7, c=9, a=1)  # argumenty przekazane po nazwie
# odejmij(a=7,b=7,1)  # SyntaxError: positional argument follows keyword argument

# print(dodaj() * odejmij(1, 2))  # TypeError: unsupported operand type(s) for *: 'NoneType' and 'NoneType'
# funkcje zwracajace wynik
print(mnozenie(8, 9))
print(mnozenie(7, 8) + mnozenie(3, 12))

a = mnozenie2(2, 3, )
print(a)  # (2, 3, 6)
a, b, c = mnozenie2(4, 5)
print(f'Wynik {a} * {b} = {c}')  # Wynik 4 * 5 = 20
