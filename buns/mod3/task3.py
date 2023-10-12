domains = input('Введите доменное имя сайта: ').split('.')
domains.reverse()
for domain in domains: print(domain)
