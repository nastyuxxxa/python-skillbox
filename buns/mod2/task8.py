input = input('Введите строку и символ через запятую: ')
counter_i = counter = index =0

for j in input:
    if j == ',':
        string = input[:counter]
        char = input[counter + 1:]
        break
    counter += 1

while string[index] == char:
    counter_i += 1
    index += 1

print(counter_i)

