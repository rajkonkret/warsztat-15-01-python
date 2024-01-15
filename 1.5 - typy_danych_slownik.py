# słownik
# para klucz - wartosc
# klucze nie mogą sie powtórzyc

slownik = {}  # pusty slownik
print(slownik)  # {}
print(type(slownik))  # <class 'dict'>

slownik['name'] = "Radek"
print(slownik)  # {'name': 'Radek'}
slownik['wiek'] = 39
print(slownik)

print(slownik['name'])  # Radek

print(slownik.keys())
print(slownik.values())
print(slownik.items())
# dict_keys(['name', 'wiek'])
# dict_values(['Radek', 39])
# dict_items([('name', 'Radek'), ('wiek', 39)])

# print(slownik['age'])  # KeyError: 'age'
print(slownik.get('age'))  # None
print(slownik.get('age', "default"))  # default

print(slownik.pop('wiek'))  # 39
print(slownik)  # {'name': 'Radek'}

print(slownik.popitem())
print(slownik)  # {}
