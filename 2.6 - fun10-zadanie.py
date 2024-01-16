# napisac funkcje ktora przyjmuje argumnty age, first, last
# age powinen posiadac wartośc domyslna
# z tych argumetów funkcja zbuduje słownik
# nalezy argumenty przekazywane do funkcji pobrac od uzytkownika w pętli while
# zastosowac "klawisz ucieczki"
def build_dict(first, name, age=None):
    person = {'first': first, 'name': name}
    if age:
        person['age'] = age
    return person


print(build_dict("Radek", "Kowalski"))  # {'first': 'Radek', 'name': 'Kowalski'}

while True:
    print("Podaj imie i nazwisko")
    print("wpisz q by zakończyc")

    f_name = input("imię")
    if f_name == 'q':
        break
    l_name = input("Nazwisko")
    if l_name == 'q':
        break
    age = input("Wiek")
    if age == 'q':
        break
    print(build_dict(f_name, l_name, age))
