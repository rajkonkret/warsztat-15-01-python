# petle
# for - petla iteracyjne
for i in range(10):  # 0..9
    print(i)

for i in range(1, 10):  # 1..9
    print(i)

for i in range(10):  # 0..9
    for j in range(10):
        print(i, j)

# list comprehesion
lista2 = [j for j in range(10)]
print(lista2)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for c in lista2:
    print(c)

for i in range(1, 10, 2):  # start, stop, krok
    print(i)
