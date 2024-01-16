# lambda - skrocony zapis funkcji
# mozliwosc uzycia funkcji w miejscu deklaracji
from functools import reduce, lru_cache


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

lata = [(2000, 29.7), (2001, 33.12), (2010, 32.92)]
print(max(lata))  # (2010, 32.92)
print(min(lata))  # (2000, 29.7)
print(max(lata, key=lambda c: c[1]))  # (2001, 33.12)
print(max(map(lambda c: (c[1], c), lata)))  # (33.12, (2001, 33.12))
print(max(map(lambda c: (c[1], c[0]), lata)))  # (33.12, 2001)


def iloczyn(a, b):
    return a * b


# reduce()
liczby = [1, 2, 3, 4, 5]
wynik = reduce(iloczyn, liczby)
print(wynik)  # 120


@lru_cache(maxsize=1000)
def fib_cached(n):
    if n < 2:
        return n
    return fib_cached(n - 1) + fib_cached(n - 2)


print(fib_cached(10))
print(fib_cached.cache_info())
# CacheInfo(hits=8, misses=11, maxsize=1000, currsize=11)
# hits - ile razy uzyskał wynikał nie muszac wykonywac obliczen
# misses - tyle razy musial na nowo obliczyc
