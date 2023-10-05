input = input('Введите слова через пробел: ')
result = ''

for i in range(len(input)):
    if input[i] == ' ':
        result += input[i - 1]
    if i == len(input) - 1:
        result += input[i]

print(result)