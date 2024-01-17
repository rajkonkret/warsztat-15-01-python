import pickle
from kl15 import Person

with open('dane.pickle', 'rb') as file:
    p = pickle.load(file)

print(p)
print(type(p))  # <class 'list'>

for person in p:
    print(person)
# Person(first_name='Jan', last_name='Kowalski', id=1)
# Person(first_name='Maciej', last_name='Nowak', id=2)

for person in p:
    person.greets()

# Witam, jestem Jan Kowalski
# Witam, jestem Maciej Nowak
# ------
# [Person(first_name='Jan', last_name='Kowalski', id=1), Person(first_name='Maciej', last_name='Nowak', id=2)]
# <class 'list'>
# Person(first_name='Jan', last_name='Kowalski', id=1)
# Person(first_name='Maciej', last_name='Nowak', id=2)
# Witam, jestem Jan Kowalski
# Witam, jestem Maciej Nowak
