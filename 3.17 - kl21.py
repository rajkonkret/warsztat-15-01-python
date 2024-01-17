from functools import total_ordering


class MyNumber:
    def __init__(self, value):
        self.value = value


print(5 < 15)  # True
num1 = MyNumber(5)
num2 = MyNumber(15)


# TypeError: '<' not supported between instances of 'MyNumber' and 'MyNumber'
# print(num1 < num2)

@total_ordering
class MyNumber2:
    def __init__(self, value):
        self.value = value

    # wykona dla porównania <
    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value


num3 = MyNumber2(5)
num4 = MyNumber2(15)
num5 = MyNumber2(15)
print(num3 < num4)  # True
print(num4 == num5)  # False, on porównał w ten sposób referencje
# zeby porównał obiekty jako wartosci musimy dodac __eq__
print(num4 == num5)  # wtedy wynik True
print(num5 > num3)
