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
