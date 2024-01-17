import pickle
from dataclasses import dataclass


# class Person:
#     def __init__(self, fn, ln, id):
#         self.fn = fn
#         self.ln = ln
#         self.id = id
#
#
# p1 = Person("Jan", "Kowalski", 1)
# print(p1)  # <__main__.Person object at 0x000001B13FE71280>

@dataclass
class Person:
    first_name: str
    last_name: str
    id: int


p2 = Person("Jan", "Kowalski", 1)
print(p2)  # Person(first_name='Jan', last_name='Kowalski', id=1)
p3 = Person("Maciej", "Nowak", 2)

people = [p2, p3]
print(people)
# [Person(first_name='Jan', last_name='Kowalski', id=1),
# Person(first_name='Maciej', last_name='Nowak', id=2)]

with open("dane.pickle", "wb") as stream:
    pickle.dump(people, stream)