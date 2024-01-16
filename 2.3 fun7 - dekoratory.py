# dekoratory - funkcje, które dodają nowe funkcjonalnosci do istniejacych funkcji
# dekoratory wykorzystuja zasaddy funkcji wewnetrznej

def dekor(funk):
    def wew():
        print("Dekorujemy!!!")
        return funk()

    return wew  # zwraca adres funkcji wewnętrznej


@dekor  # dodalismy dekorator o nazwie dekor
def hej():
    print("Hej!!!")


hej()
# Dekorujemy!!!
# Hej!!!
