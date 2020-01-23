"""
Дано N человек, считалка из K слогов.
Считалка начинает считать с первого человека. Когда считалка досчитывает до k-го слога,
человек, на котором она остановилась, вылетает. Игра происходит до тех пор, пока не останется
последний человек.
Для данных N и К дать номер последнего оставшегося человека.
"""

def count_man_old(n: int, k: int) -> int:
    man = [i + 1 for i in range(n)]
    while len(man) > 1:
        j = 0
        if k < len(man)::
            j = k - 1
            man.pop(j)
        elif k == len(man):
            man.pop()
        else:
            j = k - len(man) -1
            man.pop(j)
        man = man[j:] + man[0:j]
    return man[0]


if __name__ == "__main__":
    n = 5
    k = 3
    print(count_man(n, k))
