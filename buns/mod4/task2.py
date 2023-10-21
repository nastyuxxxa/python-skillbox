def exponentiation(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return exponentiation(a ** 2, n // 2)
    else:
        return a * exponentiation(a, n - 1)


a, n = map(int, input("Введите через пробел число и в какую степень его возвести: ").split(" "))
print(exponentiation(a, n))