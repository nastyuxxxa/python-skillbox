string = input('Введите строку из 0 и 1: ')
print("yes" if string.count('1') == string.count('0') else "no")