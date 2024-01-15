import sys

print("Nazywam się Radek")  # Nazywam się Radek
print(type("Radek"))  # <class 'str'>
print(type('Radek'))  # <class 'str'> czyli tekstowy
print(39)  # 39
print(type(39))  # <class 'int'> liczby całkowite
print(sys.int_info)  # informacja o typie int  w pythonie
# sys.int_info(bits_per_digit=30, sizeof_digit=4, default_max_str_digits=4300, str_digits_check_threshold=640)
print(type("93"))  # <class 'str'>
# print("93" + 45)  # TypeError: can only concatenate str (not "int") to str
print("93" + "45")  # konkatenacja tekstów 9345 - łaczenie
print(93 + 45)  # 138
# silne typowanie - nie z amienia sam typów
# musimy jawnie wskazac zamiane
print(int("93") + 45)  # int() - rzutowanie, zamiana na int
print(str("93") + "45")  # str() - rzutowanie na str 9345
print(5 * "93")  # 9393939393 powielanie tekstów
# zmiennej - pudełko przechowujące dane
name = "Radek"  # przypisanie wartości do zmiennej
print(name)  # wypisanie wartości zmiennej, Radek
print(type(name))  # <class 'str'>
name = 39
print(name)
print(type(name))  # <class 'int'>
# typowanie dynamiczne - mozna w kazdej chwili wrzucic inny typ danych do zmiennej
# print(name + "Tomek")  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

wiek = 45
rok = 2023
temp = 36.6  # float - zmiennoprzecinkowy
print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021,
#                min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)
temp2 = 36, 6  # to nie jest liczba!!! krotka(tupla)
# typ zmiennoprzecinkowy rozdzielane kropką
# 11:30
print(0.1 + 0.5)  # 0.6
print(0.1 + 0.7)  # 0.7999999999999999
print(0.1 + 0.2)  # 0.30000000000000004
# bład zaookrąglenia
# decimal - typ liczbowy do obliczen z ominięciem problemu liczb typu float

print(wiek + rok)
print(wiek - rok)
print(wiek / rok)  # wynik -> float
print(wiek * rok)
print(wiek // rok)  # 0, czesc calkowita z dzielania, dzielenie bez reszty
print(wiek ** rok)  # potęgowanie
print(len(str(wiek ** rok)))  # 3345

print(54 - 5 * 43 / 2 + 4 / 2)
print(54 - (5 * 43) / (2 + 4) / 2)
# -51.5
# 36.08333333333333

wersja = 3.90001  # float
print(
    f"Używamy wersji pythona {wersja}")  # f-string, w klamerkach mozemy umiescic zmienne/wyrazenia i wynik zostanie wypisany w tym miejscu
# Używamy wersji pythona 3.90001
print(f"Używamy wersji pythona {wersja:.1f}")  # Używamy wersji pythona 3.9
print(f"Używamy wersji pythona {wersja:.2f}")  # Używamy wersji pythona 3.90
print('Uzywamy:', wersja)
print("Uzywamy %f" % wersja)  # weryfikuje typ %f - oznacze ze oczekiwuje float, jest lazy
print("UZywamy wersji pyrhon {}".format(wersja))
print(f"""Tekst wielolinijkowy
    {wersja}""")
# Tekst wielolinijkowy
#     3.90001
imie = "Radek Radek"
print(imie.upper())  # RADEK RADEK

liczba = 456789123456
# print(liczba.upper())  # AttributeError: 'int' object has no attribute 'upper'
print(liczba)  # 456789123456
print(f"Nasza duza liczba {liczba:,}")  # Nasza duza liczba 456,789,123,456
print(f"Nasza duza liczba {liczba:,}".replace(",", "."))  # Nasza duza liczba 456.789.123.456

# typ logiczny
# True False -> prawda, fałsz
czy_znasz_python = True  # w pythonie obowiązkowo z dużej litery
print(czy_znasz_python)  # True
print(type(czy_znasz_python))  # <class 'bool'>print typ logiczny

print(int(True))  # 1
print(int(False))  # 0
print(bool(1))  # True  bool() - rzutowanie na typ logiczny
print(bool(0))  # False
print(bool(100))  # True
print(bool(-10))  # True
print(bool("radek"))  # True
print(bool(""))  # False
print(bool(None))  # False
# None - null - nic, stan nieokreslony

tekst = "      Tekst     "
print(tekst.strip())  # "Tekst"

tekst_x = "Witaj świecie"
encode_s = tekst_x.encode('utf-8')
print(encode_s)  # b'Witaj \xc5\x9bwiecie'
print(encode_s.decode('utf-8'))  # "Witaj świecie"
# \xc5 - zapis szesnastkowy wartości bajtu 197
# \x - zapis szesnatkowy
