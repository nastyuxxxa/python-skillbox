def make_palindrome(word):
    counter = {}
    single_char = ""
    result = ""

    for char in word:
        if char not in counter:
            counter[char] = 1
        else:
            counter[char] += 1
            if counter[char] == 2:
                counter[char] = 0
                result += char

    for char, count in counter.items():
        if count == 1:
            single_char = char
            break

    if len(result) > 1:
        return result + single_char + result[::-1]
    else:
        return f"Из слова {word} нельзя составить палиндром"


word = input("Введите слово: ")

if word == word[::-1]:
    print(f"Слово {word} является палиндромом")
else:
    print(make_palindrome(word))