nums = list(map(int, input("Введите последовательность чисел через пробел: ").split(' ')))
print(len(nums) != len(set(nums)))