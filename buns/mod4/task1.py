def check_numbers(numbers):
    unique_numbers = set(numbers)
    if len(unique_numbers) == 1:
        return "Все числа равны"
    elif len(unique_numbers) == len(numbers):
        return "Все числа разные"
    else:
        return "Есть равные и неравные числа"


numbers = input("Введите несколько чисел через пробел: ").split()
print(check_numbers(numbers))