# hermetezycja, enkapsulacja
class Boat:
    """
    klasa łodka
    """

    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.__speed = 0  # pole prywatne

    def sail(self):
        self.__speed += 10

    def speedometer(self):
        print(f"Speed in knots {self.__speed}")


boat = Boat("Omega", "2023")
boat.sail()
boat.sail()
boat.sail()
boat.sail()
boat.sail()
# print(boat.__speed)  # 50  AttributeError: 'Boat' object has no attribute '__speed' po oznaczeniu jako pole prywatne
boat.speedometer()  # Speed in knots 50
boat.__speed = 0  # przypadkowo stworzenie pola o tej samej nazwie, ale to pole ma zasieg globalny,
# nie wplywa na prywatne pole __speed
# boat.__speed = 200
boat.speedometer()  # Speed in knots 50
