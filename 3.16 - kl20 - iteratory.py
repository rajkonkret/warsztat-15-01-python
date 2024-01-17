lista = [1, 2, 3, 4, 5]
iterator = iter(lista)
print(iterator)  # <list_iterator object at 0x000001F85D466D70>
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print("Zrób coś")
print(next(iterator))


# print(next(iterator))  # StopIteration

class Count:
    def __init__(self, lows, high):
        self.current = lows
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


print("-------")
counter = Count(1, 5)
print(next(counter))
print(next(counter))
print(next(counter))
