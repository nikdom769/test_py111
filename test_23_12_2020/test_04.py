"""
Дана плоская квадратная двумерная сетка (массив),
на которой определена стоимость захода в каждую ячейку (все стоимости положительные).
Необходимо найти путь минимальной стоимости из заданной ячейки в заданную ячейку и вывести этот путь.
"""

def calculate_paths(shape: (int, int), point: (int, int)) -> list:

    steps = []
    field = [[2, 7, 9, 3],
             [14, 4, 1, 9],
             [1, 5, 2, 5]]

    for i in range(1, shape[1]):
        field[0][i] = field[0][i] + field[0][i - 1]

    for j in range(1, shape[0]):
        field[j][0] = field[j][0] + field[j - 1][0]

    #print(field)

    for i in range(shape[1] - 1):
        for j in range(shape[0] - 1):
            right = field[i][j + 1]
            down = field[i + 1][j]
            #print(right, down)
        if right < down:
            field[i + 1][j + 1] += right
            steps.append((i + 1, j + 1))
        else:
            field[i + 1][j + 1] += down
            steps.append((i, j))


    print(field)
    print(steps)


    return field[point[0]][point[1]]


if __name__ == "__main__":
    calculate_paths((3, 4), (3, 4))