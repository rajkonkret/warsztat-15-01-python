# lambda - skrocony zapis funkcji
# mozliwosc uzycia funkcji w miejscu deklaracji

def liczymy(x, y):
    return x * y


print(liczymy(5, 6))

liczymy2 = lambda x, y: x * y  # lambda ma return z automatu
print(liczymy2(6, 7))

lista = [1, 2, 3, 4, 5, 6, 7, 20, 55, 100, 123]
# przemnożenie tych liczb przez 2
lista2 = []
for i in lista:
    lista2.append(i * 2)
print(lista2)  # [2, 4, 6, 8, 10, 12, 14, 40, 110, 200, 246]

print([i * 2 for i in lista])


def zmien(x):
    return x * 2


print([zmien(i) for i in lista])  # [2, 4, 6, 8, 10, 12, 14, 40, 110, 200, 246]
# funkcje wyzszego rzedu
# map() - bierze element kolekcji i wykonuje na nim operacja zadana funkcja
print(f"Uzycie map() {list(map(zmien, lista))}")
# Uzycie map() [2, 4, 6, 8, 10, 12, 14, 40, 110, 200, 246]
# lambda jako funkcja anonimowa, uzycie w miejscu deklaracji
print(f"Uzycie map() z lambda {list(map(lambda x: x * 2, lista))}")
# Uzycie map() z lambda [2, 4, 6, 8, 10, 12, 14, 40, 110, 200, 246]

# filter() - filtruje kolekcje wg zadanego warunku
print(f"Użycie filter() {list(filter(lambda x: x > 8, lista))}")
# Użycie filter() [20, 55, 100, 123]
print(f"Użycie filter() {list(filter(lambda x: x < 30, lista))}")
# Użycie filter() [1, 2, 3, 4, 5, 6, 7, 20]
print(f"Użycie filter() {list(filter(lambda x: 3 < x < 30, lista))}")
# wieksze od 3, mniejsze od 30
# Użycie filter() [4, 5, 6, 7, 20]
print(f"Uzycie map() z lambda {list(map(lambda x: x ** 2, lista))}")
# Uzycie map() z lambda [1, 4, 9, 16, 25, 36, 49, 400, 3025, 10000, 15129]

r0 = {'miasto': "Kielce"}
r1 = {'miasto': "Kielce", "ZIP": "25-900"}
print(r0['miasto'])
print(r1['miasto'])
# print(r0['ZIP'])  # KeyError: 'ZIP'

print(r0.get('ZIP', '00-000'))
d_zip = lambda row: row.setdefault("ZIP", "00-000")
print(d_zip(r0))
print(d_zip(r1))
print(r0)
print(r1)
# {'miasto': 'Kielce', 'ZIP': '00-000'}
# {'miasto': 'Kielce', 'ZIP': '25-900'}
