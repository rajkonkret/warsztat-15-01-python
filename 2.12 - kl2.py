class Contact:
    all_contact = []  # pusta lista, jest wspólna dla wszytskich obiektów

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contact.append(self)

    def __repr__(self):  # nadpisanie __repr__ nadpisuje __str__ jesli nie zrobilismy włąsnego __str__
        return f"{self.name} {self.email}"


class Suplier(Contact):
    """
    Klasa dziedziczy z kalsy Contact
    """

    def order(self, order):
        print(f"{order} zamówiono od {self.name}")


c1 = Contact("Adam", "admin@wp.pl")
print(c1)
c2 = Contact("Radek", "radek@wp.pl")
c3 = Contact("Tomek", "admin@wp.pl")
print(c1.all_contact)  # [Adam admin@wp.pl, Radek radek@wp.pl, Tomek admin@wp.pl]
print(c3.all_contact)  # [Adam admin@wp.pl, Radek radek@wp.pl, Tomek admin@wp.pl]
s1 = Suplier("Marek", "marek@wp.pl")
print(s1)  # Marek marek@wp.pl
print(s1.all_contact)  # [Adam admin@wp.pl, Radek radek@wp.pl, Tomek admin@wp.pl, Marek marek@wp.pl]
# dopisac do klasy Suplier metode order
# metada ma przyjmowac zamowienie (kawa)
# ma wypisywac ze taki to a taki zamówił to
# Kawa zamoiona przez Marek
s1.order("Kawa")  # Kawa zamówiono od Marek
