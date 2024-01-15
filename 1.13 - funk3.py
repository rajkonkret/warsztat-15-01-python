def example(a, b, /, d=0, **kwargs):  # ** argumenty słownika
    print("a, b", a, b)
    print("d", d)
    print("kwargs", kwargs)


example(1, 2)
# / oddziela argumenty pozycyjne od nazwanych
# example(b=3, a=4)  # TypeError: example() missing 2 required positional arguments: 'a' and 'b'
example(1, 2, d=8)  # d 8
example(1, 2, d=9, a=10)  # kwargs {'a': 10}


def allparams(*args, **kwargs):
    print(args, kwargs)


allparams(1, 2, 3, 4, a=8, b=9)  # (1, 2, 3, 4) {'a': 8, 'b': 9}
print(example.__code__.co_varnames)  # ('a', 'b', 'd', 'kwargs')
print(allparams.__code__.co_varnames)  # ('args', 'kwargs')
