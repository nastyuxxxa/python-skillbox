def nod(n1, n2):
    (maximum, minimum) = (max(n1, n2), min(n1, n2))
    if maximum % minimum == 0:
        return minimum
    else:
        return nod(minimum, maximum % minimum)


n1, n2 = map(int, input("Введите два числа через пробел: ").split(" "))
print("НОД двух чисел равен:", nod(n1, n2))