input = input('Введите строку из 0 и 1: ')
count_0 = count_1 = 0

for i in input:
    if i == '0':
        count_0 += 1
    if i == '1':
        count_1 += 1

if count_1 == count_0:
    print('yes')
else:
    print('no')