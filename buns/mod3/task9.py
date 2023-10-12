N = int(input("Введите кол-во сделанных роботом шагов: "))

with open('output9.txt', 'w') as file:
    square_size = 1 #размер квадарата, по которому движется робот
    steps_count = 0 #счётчик шагов
    x = y = 0
    dx, dy = -1, 0
    directions = {
        (-1, 0): (0, -1),
        (0, -1): (1, 0),
        (1, 0): (0, 1),
        (0, 1): (-1, 0)
    }

    for i in range(N):
        x += dx
        y += dy
        steps_count += 1
        if steps_count == square_size:
            dx, dy = directions[(dx, dy)]
            steps_count = 0
            if (dx, dy) == (1, 0) or (dx, dy) == (-1, 0):
                square_size += 1

    file.write(f'{x} {y}')