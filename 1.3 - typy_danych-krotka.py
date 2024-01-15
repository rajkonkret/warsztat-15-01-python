# krotka - kolekcja przecowujca dane, niezmienna - immutable
tupla = "Radek", "tomek", "Zenek", "Marek"
print(type(tupla))  # <class 'tuple'>
print(tupla)  # ('Radek', 'tomek', 'Zenek', 'Marek')
tupla2 = 'Radek'
print(type(tupla2))  # <class 'str'>
tupla3 = "Radek",
print(type(tupla3))
print(tupla3)  # ('Radek',)
tupla4 = ("Radek",)  # PEP8 zaleca do tupli jednoelemntowych nawiasy ()
print(tupla4)

print(tupla.count("Radek"))
print(tupla.index("Radek"))

# rozpakowanie tupli
a, b = 1, 2
print(a)
print(b)

# a, b = 1, 2, 3  # ValueError: too many values to unpack (expected 2)
a, *b = 1, 2, 3
print(a)  # 1
print(b)  # [2, 3] - worek na pozostałe dane

# tupla = "Radek", "tomek", "Zenek", "Marek"
imie1, *imie2, imie3 = tupla
print(imie1)  # Radek
print(imie2)  # ['tomek', 'Zenek']
print(imie3)  # Marek

lista = list(tupla)
print(lista)  # ['Radek', 'tomek', 'Zenek', 'Marek']
print(type(lista))  # <class 'list'>
