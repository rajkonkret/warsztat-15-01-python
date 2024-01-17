from abc import ABC, abstractmethod


class Counter(ABC):
    def __init__(self, values=0):
        self.values = values

    def increment(self, by=1):
        self.values += by

    @abstractmethod  # metoda abstrakcyjna, obowiazkowo musimy nadpisac ja w klasach dziedziczacych
    def drukuj(self):
        pass

    @staticmethod  # metoda statyczna
    def from_string():
        print("Metoda statyczna")

    @classmethod
    def from_counter(cls, counter):
        return cls(counter.values)


class BoundedCounter(Counter):
    MAX = 100

    def __init__(self, values=0):
        if values > self.MAX:
            raise ValueError(f"Wartośc nie może być większa od {self.MAX}")
        super().__init__(values)

    def drukuj(self):
        print("Drukuje", self.values)


# nie da sie stworyzc obiektu klasy NewCounter bo nie ndpisał metodu drukuj()
class NewCounter(Counter):
    """
    klasa dziedziczy po Counter
    """


# nie mozna stworzyc obiektu klasy abstrakcyjnej
# TypeError: Can't instantiate abstract class Counter without an implementation for abstract method 'drukuj'
# c1 = Counter()
# c1.increment()
# c1.drukuj()

bc = BoundedCounter()
bc.drukuj()
# nie nadpisałem metody drukuj, program nie bedzie działać
# nc = NewCounter()  # TypeError: Can't instantiate abstract class NewCounter without an implementation for abstract method 'drukuj'
Counter.from_string()  # Metoda statyczna
bc2 = BoundedCounter()
bc2.increment()
bc2.increment()
bc2.increment()
bc2.increment()
a = bc.from_counter(bc2)
a.drukuj()  # Drukuje 4
b = BoundedCounter.from_counter(bc2)  # metoda classmethod tez jest statyczna
b.drukuj()  # Drukuje 4
