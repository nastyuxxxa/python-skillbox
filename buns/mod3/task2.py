num = input('Введите натурально число: ')
num = int(num) if num.isdigit() else num
print(f"{bin(num)[2:]}, {oct(num)[2:]}, {hex(num)[2:]}" if isinstance(num, int)  else "Неверный ввод")