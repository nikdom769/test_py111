"""
Дано N человек, считалка из K слогов.
Считалка начинает считать с первого человека. Когда считалка досчитывает до k-го слога,
человек, на котором она остановилась, вылетает. Игра происходит до тех пор, пока не останется
последний человек.
Для данных N и К дать номер последнего оставшегося человека.
"""

def count_man_old(n: int, k: int) -> int:
    man = [i + 1 for i in range(n)]
    print(man)
    while len(man) > 1:
        if len(man) < k and len(man) > 1:
            j = k - len(man)
            print(j)
            man.pop(j - 1)
        else:
            man.pop(k - 1)
    #print(man[0])
    return man[0]


def count_man(n: int, k: int) -> int:
    man = [i + 1 for i in range(n)]
    print(man)
    j = 0 # позиция участника игры
    while len(man) > 1:
        if len(man) < k and len(man) > 1:
            j += k - len(man)
            #print(j)
            man.pop(j - 1)
        else:
            if j + k - 1 < len(man):
                j += k - 1
                man.pop(j)
            else:
                j = j + k - 1 - len(man)
                man.pop(j)

    #print(man[0])
    return man[0]




if __name__ == "__main__":
    n = 5
    k = 3
    print(count_man(n, k))
