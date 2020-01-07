import random
from typing import Collection, TypeVar

_Tt = TypeVar("_Tt")


def sort(container: Collection[_Tt]) -> Collection[_Tt]:
    """
    Sort input container with quick sort
    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if len(container) > 1:
        pivot = container[len(container)//2]
        i = 0
        j = len(container) - 1
        first = []
        last = []
        while i < j: 
            if i < len(container) // 2:
                first.append(container[i]) if container[i] < pivot else last.append(container[i])
            if j > len(container) // 2:
                last.append(container[j]) if container[j] >= pivot else first.append(container[j])
            i += 1
            j -= 1 
        return sort(first) + [pivot] + sort(last) 
    else:
        return container


if __name__ == "__main__":
    arr = [random.randint(-100, 100) for _ in range(15)]
    print(arr)
    print(sort(arr))

