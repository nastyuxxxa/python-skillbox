input = input('Введите слова кириллицей в нижнем регистре через пробел: ')
consonant_letters ='йцкнгшщзхфвпрлджчсмтб'
vowel_letters = 'ёуеыаоэяию'
counter_cons = counter_vowel = 0

for i in range(len(input)):
    if input[i] in consonant_letters:
        counter_cons += 1
    if input[i] in vowel_letters:
        counter_vowel += 1

print(counter_vowel, counter_cons)