# while - petla sterowana warunkiem

licznik = 0
while licznik < 10:
    licznik += 1
    print("Komunikat")

print(licznik)  # 10

lista = []
lista2 = []
while True:
    print("Działam")
    wej = input("Podaj liczbę")  # str
    if not wej.isnumeric():
        break

    lista.append(wej)
    lista2.append(int(wej))
print(lista)  # ['1', '2', '3', '4', '5', '6'] str
print(lista2)  # [1, 2, 3, 4, 5, 7] int
