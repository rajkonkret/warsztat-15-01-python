from pprint import pprint


class ContactList(list['Contact']):
    def search(self, name):
        matching_contact = []
        for c in self:
            if name in c.name:
                matching_contact.append(c)
        return matching_contact


class Contact:
    all_contact = ContactList()  # pusta lista typu ContactList, posiada metode search,

    # jest wspólna dla wszytskich obiektów

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contact.append(self)

    def __repr__(self):  # nadpisanie __repr__ nadpisuje __str__ jesli nie zrobilismy włąsnego __str__
        return f"{self.name!r} {self.email!r}"  # ['Adam' 'admin@wp.pl']


class Suplier(Contact):
    """
    Klasa dziedziczy z kalsy Contact
    """

    def order(self, order):
        print(f"{order} zamówiono od {self.name}")


class Friend(Suplier):
    """
    Klasa dziedziczy po Suplier
    """

    def __init__(self, name, email, phone='000000000'):
        super().__init__(name, email)
        self.phone = phone

    def __repr__(self):  # nadpisanie __repr__ nadpisuje __str__ jesli nie zrobilismy włąsnego __str__
        return f"{self.name!r} {self.email!r}, +48{self.phone}"  # ['Adam' 'admin@wp.pl']


lista = []
# print(lista.search())  # AttributeError: 'list' object has no attribute 'search'

lista2 = ContactList()
print(lista2.search("Radek"))  # []
print(lista2)
print(type(lista2))  # <class '__main__.ContactList'>

c1 = Contact("Adam", "admin@wp.pl")
print(c1)
c2 = Contact("Radek", "radek@wp.pl")
c3 = Contact("Tomek", "admin@wp.pl")
print(c1.all_contact)  # [Adam admin@wp.pl, Radek radek@wp.pl, Tomek admin@wp.pl]
print(c3.all_contact)  # [Adam admin@wp.pl, Radek radek@wp.pl, Tomek admin@wp.pl]
s1 = Suplier("Marek", "marek@wp.pl")
print(s1)  # Marek marek@wp.pl
print(s1.all_contact)  # [Adam admin@wp.pl, Radek radek@wp.pl, Tomek admin@wp.pl, Marek marek@wp.pl]
print(c1.all_contact.search("Adam"))  # [Adam admin@wp.pl]
print(ContactList.__mro__)  # (<class '__main__.ContactList'>, <class 'list'>, <class 'object'>)
print(Suplier.__mro__)  # (<class '__main__.Suplier'>, <class '__main__.Contact'>, <class 'object'>)
f1 = Friend("Kasia", 'kasia@wp.pl')
f1.order("Herbata")  # Herbata zamówiono od Kasia
f2 = Friend("Jarek", "admin2@wp.pl", "899098765")
print(f2)  # 'Jarek' 'admin2@wp.pl', +48899098765
print(s1.all_contact)
pprint(s1.all_contact)
# ['Adam' 'admin@wp.pl',
#  'Radek' 'radek@wp.pl',
#  'Tomek' 'admin@wp.pl',
#  'Marek' 'marek@wp.pl',
#  'Kasia' 'kasia@wp.pl', +48000000000,
#  'Jarek' 'admin2@wp.pl', +48899098765]
