# dekortor, ktory zmienia tekst na duze litery
# funkcja zwraca tekst a my ten tekst w dekoratorzy zamieniamy na duze litery i zwracy zamieniony tekst
def uppercase_decorator(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return result.upper()

    return wrapper


def bold_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"\033[1m" + result + "\033[0m"

    return wrapper


@uppercase_decorator
def greeting():
    return "Hello World!"


@bold_decorator
@uppercase_decorator
def greeting2(name):
    return name


print(greeting())  # HELLO WORLD!
print(greeting2("Radek"))
