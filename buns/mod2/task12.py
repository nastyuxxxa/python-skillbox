phone_number = input('Введите номер телефона: ')
result = ''
symbols = '()- '

for i in phone_number:
    if i not in symbols:
        result += i

print(result)

