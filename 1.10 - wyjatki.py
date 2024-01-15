# wyjatki
try:
    # print("12" + 34)
    # print(34 / 0)
    # print(int("A"))
    # print("A")
    raise KeyError("Bląd klucza")  # rzucenie błedu
except TypeError:
    print("Bład typu")
except ZeroDivisionError:
    print("Nie dziel przez zero")
except ValueError:
    print("Bład wartości")
except Exception as e:
    print("Bład", e)
else:
    print("Nie było błedu")
finally:
    print("Wykona sie zawsze")

print("Program działa nadal")
