# generatory -

def kwadrat(n):
    for x in range(n):
        print(x ** 2)


kwadrat(5)


def kwadrat2(n):
    for x in range(n):
        yield x ** 2


kwa = kwadrat2(5)
print(next(kwa))
print(next(kwa))
print(next(kwa))
print('Wykonaj cokolwiek')
lista = []
print(lista)
lista.append("123456")
print(lista)

print(next(kwa))  # 9

kwa2 = kwadrat2(5)
print(next(kwa2))
print(next(kwa2))
print(next(kwa2))
try:
    print(next(kwa2))
    print(next(kwa2))
    print(next(kwa2))
except StopIteration:
    print("Zakończyłem działanie")
