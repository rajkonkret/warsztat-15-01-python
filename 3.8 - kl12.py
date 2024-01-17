# dziedziczenie diamentowe

class A:
    def method(self):
        print("Metoda kalsy A")


class B(A):
    def method(self):
        print("Metoda kalsy B")


class C(A):
    def method(self):
        print("Metoda kalsy C")


class D(B, C):
    pass


# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\warsztat-15-01-python\3.8 - kl12.py", line 22, in <module>
#     class E(A, B):
# TypeError: Cannot create a consistent method resolution
# order (MRO) for bases A, B
class E(A, B):  # abuzamy kolejnosc dla __mro__
    pass


a = A()
a.method()

b = B()
b.method()

c = C()
c.method()

d = D()
d.method()  # Metoda kalsy B
