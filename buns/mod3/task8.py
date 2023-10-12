phone_number = input('Введите номер телефона: ')
print('+' + ''.join(num for num in phone_number if num.isdigit()))