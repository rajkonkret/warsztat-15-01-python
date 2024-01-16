from itertools import zip_longest

generator_1 = [x for x in range(5)]
print(generator_1)
print(type(generator_1))  # <class 'list'>
generator_2 = (x for x in [1, 2, 3, 4, 5])
print(type(generator_2))  # <class 'generator'>
print(generator_2)  # <generator object <genexpr> at 0x000002BAD7AA4DC0>
print(next(generator_2))
print(next(generator_2))
print(next(generator_2))
print(next(generator_2))
print(next(generator_2))


# print(next(generator_2))  # StopIteration

def generator3():
    for x in [1, 2, 3, 4, 5]:
        yield x


g3 = generator3()
print(next(g3))
print(next(g3))
print(next(g3))


def gen4():
    i = 1
    while True:
        yield i * 1
        i += 1


g4 = gen4()
print(next(g4))
print(next(g4))
print(next(g4))
print(next(g4))
print(next(g4))
print(next(g4))
print(next(g4))


def fibo():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


fib1 = fibo()
print(next(fib1))
print(next(fib1))
print(next(fib1))
print(next(fib1))
print(next(fib1))
print(next(fib1))
print(next(fib1))
print(next(fib1))


def fibo_with_index(n):
    a, b = 0, 1
    for ind in range(n):
        yield ind, a
        a, b = b, a + b


fib2 = fibo_with_index(100)
print(next(fib2))
print(next(fib2))
print(next(fib2))
print(next(fib2))
print(next(fib2))
print(next(fib2))
print(next(fib2))

for i in fibo_with_index(10):
    print(f"Element {i}")  # Element (9, 34)

for i, n in fibo_with_index(10):
    print(f"Pozycja {i}, element {n}")  # Pozycja 9, element 34

fibo3 = fibo_with_index(10)
print(list(fibo3))
# [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), (8, 21), (9, 34)]
print("------------")
# list wyczerpuje generator. został wyczerpany. nie ma kolejnych danych
for i in fibo3:
    print(i)

person = ['Radek', 'Tomek', 'Zenek', 'Agnieszka', 'Krzysztof']
age = [34, 45, 23, 24]

# Radek 34
# zip()

for p, w in zip(person, age):
    print(p, w)  # Radek 34

zipped = zip_longest(person, age, fillvalue=None)
# print(zipped)
# for i in zipped:
#     print(i)
#
# print(next(zipped))
#
# print("------")
# for i in zipped:
#     print(i)
# # ('Radek', 34)
# # ('Tomek', 45)
# # ('Zenek', 23)
# # ('Agnieszka', 24)
# # ('Krzysztof', None)
zipped_list = list(zipped)
for i in zipped_list:
    print(i)
print("-------")
for i in zipped_list:
    print(i)


def counter(start=0):
    n = start
    while True:
        result = yield n
        print(result)  # None, Ok,
        if result == 'q':
            break
        n += 1


c = counter(10)
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(c.send("Ok"))
try:
    c.send('q')
except StopIteration:
    pass
print(next(c))  # StopIteration
