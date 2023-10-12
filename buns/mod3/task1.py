a, b, c = map(int, input('Введите три числа от -1000 до 1000 через пробел: ').split(' '))
numbers = sorted([a, b, c])
print(numbers[1])