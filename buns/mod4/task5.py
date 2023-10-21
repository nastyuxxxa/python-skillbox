def get_letters_statistic(file_name):
    with open(file_name, 'r') as file:
        text = "".join(filter(str.isalpha, file.read()))

    letters_counts = {}

    for letter in text:
        if letter in letters_counts:
            letters_counts[letter] += 1
        else:
            letters_counts[letter] = 1

    result = sorted(letters_counts.items(), key=lambda x: x[1])

    return result


def write_to_file(file_name, letters_statistic):
    with open(file_name, 'w') as file:
        file.writelines(f'{letter}: {count}\n' for letter, count in letters_statistic)


input_file_name = input("Введите имя файла: ")
output_file_name = 'letters_statistic.txt'
letters_statistic = get_letters_statistic(input_file_name)
write_to_file(output_file_name, letters_statistic)
