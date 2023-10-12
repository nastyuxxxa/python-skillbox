words = input("Введите слова через пробел: ").split(' ')
print(''.join(word[-1] for word in words))