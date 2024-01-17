# stworzyc słownik
# zapisac w plikuu za pomoca pickle
# odczytac za pomoca pickle
# sprawdzić typ
import pickle

slownik = {"klucz1": "wartosc1", "klucz2": "wartosc2"}

with open('dict.pkl', 'wb') as f:
    pickle.dump(slownik, f)

with open('dict.pkl', 'rb') as fh:
    data = pickle.load(fh)

print(type(data))
print(data)
# <class 'dict'>
# {'klucz1': 'wartosc1', 'klucz2': 'wartosc2'}
