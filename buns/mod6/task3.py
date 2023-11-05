def get_armstrong_numbers():
    num = 1
    while True:
        digits = [int(digit) for digit in str(num)]
        num_len = len(digits)
        summa = sum([digit ** num_len for digit in digits])
        if summa == num and num not in range(2, 10):
            yield num
        num += 1


armstrong_numbers = get_armstrong_numbers()


def armstrong_numbers_generator():
    return next(armstrong_numbers)


for i in range(8):
    print(armstrong_numbers_generator(), end=' ')