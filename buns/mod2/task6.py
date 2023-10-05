domain_name = input('Введите доменное имя сайта: ')
domain1 = domain2 = domain3 = ''
dot_count = 0

for i in domain_name:
    if i == '.':
        dot_count += 1
    else:
        if dot_count == 0:
            domain3 += i
        elif dot_count == 1:
            domain2 += i
        elif dot_count == 2:
            domain1 += i

print(domain1)
print(domain2)
print(domain3)