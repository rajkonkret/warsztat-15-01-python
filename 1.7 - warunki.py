# warunki
# if

if True:
    print("Ok")

if True:
    pass  # nic nie robi

a = 2
if a == 1:  # == czy równa się
    print(f"A równa się 1")
else:  # działanie domyslne
    print("A nie równa się 1")

a = 20
if a == 1:
    print("1")
elif a == 20:
    print("20")
else:
    print("Nie wiem")

lista = range(1, 10)
for c in lista:
    if c % 2 == 0:  # modulo, reszta z dzielenia
        print(c, "parzysta")

lista4 = [j for j in range(10) if j % 2 == 0]
print(lista4)  # [0, 2, 4, 6, 8]
