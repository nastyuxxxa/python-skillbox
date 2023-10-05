a = a1 = a2 = int(input('Введите натуральное число: '))
a_binary = a_octal = a_hex = ''
digits = "0123456789ABCDEF"

if a > 0:
    while a > 0:
        a_binary = digits[a % 2] + a_binary
        a //= 2
    while a1 > 0:
        a_octal = digits[a1 % 8] + a_octal
        a1 //= 8
    while a2 > 0:
        a_hex = digits[a2 % 16] + a_hex
        a2 //= 16
    print(a_binary, a_octal, a_hex)
else:
    print('Неверный ввод')