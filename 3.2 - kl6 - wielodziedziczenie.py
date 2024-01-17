# wielodziedziczenie

class A:
    def method(self):
        print("Metoda klasy A")


class B:
    def method(self):
        print("Metoda klasy B")


class C(B, A):  # kolejnosc ma znaczenie
    """
    klasa dziedziczy po klasie B i A
    """


class D(A, B):
    """
    Klasa dziedziczy po A i B
    """


class E(A, B):
    def method(self):
        print("Metoda z kalsy E")


class F(A, B):
    def method(self):
        B.method(self)  # jawne wywołanie metody z klasy B


class G(A, B):
    def method(self):
        super().method()  # wywołanie metody z klasy nadrzednej, czyli A
        print("Dopisane")


a = A()
a.method()  # Metoda klasy A

b = B()
b.method()  # Metoda klasy B

c = C()
c.method()  # Metoda klasy B
print(C.__mro__)  # (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

d = D()
d.method()  # Metoda klasy A
print(D.__mro__)  # (<class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

e = E()
e.method()  # Metoda z kalsy E

f = F()
f.method()  # Metoda klasy B

# Metoda klasy A
# Metoda klasy B
# Metoda klasy B
# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
# Metoda klasy A
# (<class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
# Metoda z kalsy E
# Metoda klasy B

g = G()
g.method()
# Metoda klasy A
# Dopisane
