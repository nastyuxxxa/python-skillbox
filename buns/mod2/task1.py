numbers = input('Введите 2 числа через запятую и пробел: ')
a = 0
b = 0
counter = 0

for i in numbers:
    if i == ',':
        a = int(numbers[:counter])
        b = int(numbers[counter + 2:])
    counter += 1

print(a % b)