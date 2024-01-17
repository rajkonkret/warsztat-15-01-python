# stworzyc system zarzadzania biblioteka
# dodaj ksiazke, usun ksiązke, wypozycz ksiązkę, zwroc ksiązkę
# uzyc klass np.: Book, Library
# obsłuzyc błedy
# dodac User

# Book -> author, title, isbn
# Library -> liste ksiazek, liste wypozyczonych ksiazek,

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __repr__(self):
        return f"Author: {self.author}, Tytuł: {self.title}, ISBN: {self.isbn}"


# dodaj ksiazke
# wypozycz ksiazke
class Library:
    def __init__(self):
        self.dostepne_ksiazki = []
        self.wypozyczone_ksiazki = []

    def fun_dodaj_ksiazke(self, book: "Book"):
        self.dostepne_ksiazki.append(book)

    def fun_ksiazki_do_wypozyczenia(self):
        return self.dostepne_ksiazki

    def fun_ksiazki_wypozyczone(self):
        return self.wypozyczone_ksiazki

    def fun_wypozycz_ksiazke(self, isbn):
        # usunac z listy dostepne
        # dodac do listy wypozyczone
        for book in self.dostepne_ksiazki:
            if book.isbn == isbn:
                self.dostepne_ksiazki.remove(book)
                self.wypozyczone_ksiazki.append(book)
                return book

        raise Exception("Nie ma takiej ksiązki")

    def fun_zwroc_ksiazke(self, isbn):
        for book in self.wypozyczone_ksiazki:
            if book.isbn == isbn:
                self.dostepne_ksiazki.append(book)
                self.wypozyczone_ksiazki.remove(book)
                return book

        raise Exception("Ksiązka nie jest z naszej biblioteki")


biblioteka = Library()
biblioteka.fun_dodaj_ksiazke(Book("Programowanie w pythonie", "Jan Kowalski", "1234567890"))
print(biblioteka.fun_ksiazki_do_wypozyczenia())
# [Author: Jan Kowalski, Tytuł: Programowanie w pythonie, ISBN: 1234567890]
book = biblioteka.fun_wypozycz_ksiazke("1234567890")
print("Wypozyczyłes ksiązkę", book)
print("Wypozyczone ksiazki", biblioteka.wypozyczone_ksiazki)
print("Dostępne ksiazki", biblioteka.dostepne_ksiazki)
print(biblioteka.fun_zwroc_ksiazke("1234567890"))
print("Wypozyczone ksiazki", biblioteka.wypozyczone_ksiazki)
print("Dostępne ksiazki", biblioteka.dostepne_ksiazki)

# stworzyc ksiązkę telefoniczna z wykorzystaniem petli while
# dodaj kontakt, usun kontakt, wyszukaj, wyswietl liste kontaktow
