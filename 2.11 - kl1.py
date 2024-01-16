# klasy - szablony
import math  # bibliotek do obliczen


class MyFirstClass:
    """
    Klasa w Pythonie, opisująa punkty w przestrzeni x i y
    """

    def __init__(self, x=0, y=0):
        """
        funkcja inicjalizująca (konstruktor)
        :param x: współrzędna x puntu
        :param y: współrzędna y punktu
        """
        # self.x = x
        # self.y = y
        self.move(x, y)

    def move(self, x: int, y: int) -> None:
        """
        funkcja przemiescza punkt we wskazane miejsce
        :param x:
        :param y:
        :return: None
        """
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def calculate(self, other: "MyFirstClass") -> float:
        """
        oblicznie odległosci miedzy punktami w przestrzeni euklidesowej
        :param other:
        :return:
        """
        return math.hypot(self.x - other.x, self.y - other.y)

    def __str__(self):  # opis obiektu
        return f"{self.x, self.y}"

    def __repr__(self):  # reprezentacja obiektu
        return f"Point({self.x}, {self.y})"


print(MyFirstClass.__doc__)
print(print.__doc__)

ob = MyFirstClass()
print(ob)  # <__main__.MyFirstClass object at 0x00000286E1495E80>
# po stworzeni __str__ opis wyglada tak (0, 0)
print(type(ob))
print(ob.x)
print(ob.y)
ob.move(5, 6)
print(ob)  # (5, 6)
ob.reset()
print(ob)  # (0, 0)
ob2 = MyFirstClass(5, 7)
print(ob2)  # (5, 7)
lista_punkty = [ob, ob2]
print(lista_punkty)
# [<__main__.MyFirstClass object at 0x00000149842ED8E0>, <__main__.MyFirstClass object at 0x00000149842ED8B0>]
# po utworzeniu funkcji __repr__
# [Point(0, 0), Point(5, 7)]
ob_str = str(ob)
print(ob_str)  # (0, 0)
print(ob)  # (0, 0)
print(ob.calculate(ob2))  # 8.602325267042627
# hinty nie weryfikuja typu
# ob.calculate("a")  # AttributeError: 'str' object has no attribute 'x'
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\warsztat-15-01-python\2.11 - kl1.py", line 73, in <module>
#     ob.calculate("a")
#   File "C:\Users\CSComarch\PycharmProjects\warsztat-15-01-python\2.11 - kl1.py", line 39, in calculate
#     return math.hypot(self.x - other.x, self.y - other.y)
#                                ^^^^^^^
# AttributeError: 'str' object has no attribute 'x'
