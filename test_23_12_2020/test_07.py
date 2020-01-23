import random


def msbits(nb, n):
    return (n*(nb - a) / (b - a))

def bucket_sort(A, n):
    buckets = [[] for _ in range(n)] # новый массив из n пустых элементов
    for i in range(len(A) - 1):
        if A[i] < 12:
            buckets[0].append(A[i])
    return Конкатенация массивов buckets[0], ..., buckets[n-1]

# верное решение - сортировка подсчетом
def count_sort(a: list, line: tuple) -> list:
    c = [0 for _ in range(line(1) - line(0) + 1)]
    for i in range(len(a)):
        c[a[i] - line[0]] += 1
    b = []
    for i in range(line(1) - line(0) + 1):
        for j in range(c[i]):
            b.append(i + line[0])
    return b



if __name__ == "__main__":
    line = (13, 25)
    numb = [random.randint(line[0], line[1] + 1) for _ in range(1000000)]
    #n = (line[1] - line[0]) // 2
    #bucket_sort(numb, n)
    print(count_sort(numb, line))
