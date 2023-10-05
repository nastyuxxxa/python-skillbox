input = input("Введите последовательность чисел через пробел: ")
flag = False

for i in range(len(input)):
    for j in range(i + 1, len(input)):
        if input[i] == input[j] and input[i] != ' ':
            flag = True
            break
    if flag:
        break

print(flag)