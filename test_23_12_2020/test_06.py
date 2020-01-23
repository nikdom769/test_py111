"""
Дан список заявок на использование ракетs
Вывести ответ, хватит ли вам одной ракеты, чтобы удовлетворить все заявки на этот день
"""

def func(zayavka: list) -> bool:
    res = []

    zayavka.sort(key=lambda x: x[0])
    res.append(zayavka.pop(0))
    for z in zayavka:
        print(z[0])
        print(res[0][1])
        if z[0] >= res[0][1]:
            res.append(z)
    print(res)
    return True if len(res) == len(zayavka) + 1 else False


if __name__ == "__main__":
    z = [(2, 5),
         (4, 6)]
    print(func(z))