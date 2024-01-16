# rekurencja
# funkcja wywołuja samą siebie
def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n - 1)


def nwd(a, b):
    if b == 0:
        return a
    return nwd(b, a % b)


print(silnia(5))  # 120
print(nwd(48, 18))  # 6
