# set (zbior) - brak duplikatow, przechowuje unikalne wartosci
# nie zachowuje kolejnosci przy dodawaniu elementów

lista = [44, 55, 66, 77, 33, 31, 33, 55, 11]
zbior = set(lista)
print(type(zbior))
print(zbior)  # {33, 66, 11, 44, 77, 55, 31}
zbior.add(18)
zbior.add(18)
zbior.add(45)
zbior.add(54)

print(zbior)  # {33, 66, 11, 44, 77, 45, 18, 54, 55, 31}
# usunie pierwszzy elent ze zbioru
# zwróci go nam
print(zbior.pop())  # 33
print(zbior)  # {66, 11, 44, 77, 45, 18, 54, 55, 31}

lista2 = []  # pusta lista
zb2 = set()  # pusty zbior, nie tworzymy nawiasami
print(zb2)  # set() dostaniemy słówko set a nie nawiasy dla pustego seta

zbior2 = {66, 11, 44, 55, 62, 999, 999}
print(zbior2)  # {66, 55, 999, 11, 44, 62}

print(zbior | zbior2)  # suma zbiorow {66, 999, 11, 44, 77, 45, 18, 54, 55, 62, 31}
print(zbior & zbior2)  # czesc wspolna zbiorów {66, 11, 44, 55}
print(zbior - zbior2)  # {45, 77, 18, 54, 31}
print(zbior.difference(zbior2))  # {45, 77, 18, 54, 31}
print(zbior.union(zbior2))  # suma {66, 999, 11, 44, 77, 45, 18, 54, 55, 62, 31}

# update()
zbior.update(zbior2)
print(zbior)  # dodane wartosci dwoch zbiorow {66, 999, 11, 44, 77, 45, 18, 54, 55, 62, 31}
print(zbior2)
lista = list(zbior)
print(lista)  # [66, 999, 11, 44, 77, 45, 18, 54, 55, 62, 31]
# 13:30
