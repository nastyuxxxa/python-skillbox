input = input('Введите строчной символ латинского алфавита и целое число через запятую: ')
i = input[:1]
n = int(input[2:])
alphabet = 'abcdefghijklmnopqrstuvwxyz'
index = 0

for j in range(len(alphabet)):
    if alphabet[j] == i:
        index = (j + n) % len(alphabet)

print(alphabet[index])