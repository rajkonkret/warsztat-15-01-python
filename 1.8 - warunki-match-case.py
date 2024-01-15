# match case
# od python 3.10

lang = input("Podaj znany Ci język programowania")
# input() - wczytuje dane np.: od użytkownika

match lang.lower().replace(" ", ""):
    case "java":
        print("Java")
    case "python":
        print("Python")
    case _:
        print("Domyślna wartość")
