def winner_of_tic_tac_toe(field):
    k = len(field)
    for row in field: #проходимся по строкам поля
        if len(set(row)) == 1 and row[0] != '_':
            return row[0]
    for j in range(k): #проходимся по столбикам поля
        if len({field[i][j] for i in range(k)}) == 1 and field[0][j] != '_':
            return field[0][j]
    if len({field[i][i] for i in range(k)}) == 1 and field[0][0] != '_': #проходимся по главной диагонали поля
        return field[0][0]
    if len({field[i][-i - 1] for i in range(k)}) == 1 and field[0][-1] != '_': #проходимся по побочной диагонали поля
        return field[0][-1]
    return 'Ничья'


field = []

while True:
    field.append(input())
    k = len(field[0])
    if len(field) == k:
        break

print(winner_of_tic_tac_toe(field))