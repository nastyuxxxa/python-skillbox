barcode = input('Введите последовательность чисел: ')
sum_even, sum_odd = 0, 0

for i in range(1, len(barcode) + 1):
    if i % 2 == 0:
        sum_even += int(barcode[i - 1])
    else:
        sum_odd += int(barcode[i - 1])

if (sum_odd + 3 * sum_even) % 10 == 0:
    print('yes')
else:
    print('no')

