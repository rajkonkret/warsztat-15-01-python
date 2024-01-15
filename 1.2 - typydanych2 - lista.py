# lista - moze przechowywac dowolna ilosc danych, dowolnego typu na raz
# zachowuje kolejnosc przy dodawaniu elemntów
lista = []  # pusta lista
print(lista)
print(type(lista))  # <class 'list'>

lista.append("Rsdaaek")
lista.append("Tomek")
lista.append("Marek")
lista.append("Zenek")
lista.append("Wincenty")

print(lista)  # ['Rsdaaek', 'Tomek', 'Marek', 'Zenek', 'Wincenty']
print(lista[0])  # pierwszy element z listy
print(lista[-1])  # ostatni element z listy
print(lista[0:3])  # ['Rsdaaek', 'Tomek', 'Marek']

lista[0] = "Radek"
print(lista)  # ['Radek', 'Tomek', 'Marek', 'Zenek', 'Wincenty']

a = 1
b = a
print(b)
a = 8
print(b)  # 1

# prawidłowa kopia listy
lista_copy = lista.copy()
print(lista_copy)
# to jest tylko kopiowanie referencji !!!
# lista1 i lista wskazuja na ten sam obszar w pamięci
# lista.clear()  czy sci obszar pamięci dla lista ale lista1 jest dokładnie w tym samym miejscu
# wiec również jest czyszczona
lista1 = lista
print(lista1)
# ['Radek', 'Tomek', 'Marek', 'Zenek', 'Wincenty']
lista.clear()  # usunięcie elementów listy
print(lista1)  # []
print(id(lista1))  # 2203796230528
print(lista)  # []
print(id(lista))  # 2203796230528
print(lista_copy)  # ['Radek', 'Tomek', 'Marek', 'Zenek', 'Wincenty']
print(id(lista_copy))  # 2203796551104

lista3 = "Python"
print(list(lista3))  # ['P', 'y', 't', 'h', 'o', 'n']  # rozpakowanie sekwencji

krotka = tuple(lista3)
print(krotka)  # ('P', 'y', 't', 'h', 'o', 'n')
print(type(krotka))  # <class 'tuple'>
