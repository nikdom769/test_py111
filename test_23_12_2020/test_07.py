import random

def msbits(nb, n):

    return (n*(nb - a) / (b - a))




def bucket_sort(A, n):
    buckets = [[] for _ in range(n)] # новый массив из n пустых элементов
    for i in range(len(A) - 1):
        if A[i] < 12:
            buckets[0].append(A[i])



  return Конкатенация массивов buckets[0], ..., buckets[n-1]


if __name__ == "__main__":
    line = (13, 25)
    numb = [random.randint(line[0], line[1] + 1) for _ in range(1000000)]
    n = (line[1] - line[0]) // 2
    bucket_sort(numb, n)