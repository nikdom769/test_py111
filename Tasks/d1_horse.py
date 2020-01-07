def calculate_paths(shape: (int, int), point: (int, int)) -> int:
    """
    Given field with size rows*cols count available paths from (0, 0) to point
    :param shape: tuple of rows and cols (each from 1 to rows/cols)
    :param point: desired point for horse
    :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
    """
    
    field = [[0]*shape[1] for _ in range(shape[0])]
    field[0][0] = 1
    #print(field)
    #steps = ((1, 2), (1, -2), (2, 1), (2, -1))
    #s_point = [0, 0]
    for i in range(shape[0]): # проход по строкам
        for j in range(shape[1]): # проход по столбцам
            # проверка точек на возможность хода из нее
            if field[i][j] != 0:
                # условия ходов (см. лекцию)
                if i + 1 < shape[0] and j + 2 < shape[1]:
                    field[i + 1][j + 2] += field[i][j] * 2
                if i + 1 < shape[0] and j - 2 >= 0:
                    field[i + 1][j - 2] += field[i][j] * 2
                if i + 2 < shape[0] and j + 1 < shape[1]:
                    field[i + 2][j + 1] += field[i][j] * 2
                if i + 2 < shape[0] and j - 1 >= 0:
                    field[i + 2][j - 1] += field[i][j] * 2
    
    #print(shape, point)
    return field[point[0]][point[1]]


if __name__ == "__main__":
    print(calculate_paths((9, 9), (8, 8)))
    print(calculate_paths((17, 12), (16, 9)))
    print(calculate_paths((12, 10), (11, 9)))
