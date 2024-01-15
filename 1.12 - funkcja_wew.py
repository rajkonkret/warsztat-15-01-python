# funkcja wewnętrzna
def fun1():  # deklaracja funkcji 1
    print("To jest fun1")

    def fun2():  # deklaracja funkcji 2
        print("To jest fun2")

    return fun2  # zwracamy referencje do fun2, czyli adres w pamieci


xFun = fun1()  # To jest fun1
print(xFun)  # <function fun1.<locals>.fun2 at 0x00000175D0508C20>
print(type(xFun))  # <class 'function'>
xFun()  # To jest fun2
