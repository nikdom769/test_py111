from typing import Collection, TypeVar

_Tt = TypeVar("_Tt")


def merge(a: Collection[_Tt], b: Collection[_Tt]) -> Collection[_Tt]:
    cont = []
    i = 0
    j = 0
    while True:
        if i == len(a) and b:
            cont.extend(b[j:])
            return cont
        elif j == len(b) and a:
            cont.extend(a[i:])
            return cont
        elif i <= len(a) and a[i] <= b[j]:
            cont.append(a[i])
            i += 1
        elif j < len(b) and b[j] < a[i]:
            cont.append(b[j])
            j += 1



def sort(container: Collection[_Tt]) -> Collection[_Tt]:
    """
    Sort input container with merge sort
    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if len(container) >= 2:
        return merge(sort(container[:len(container)//2]), sort(container[len(container)//2:]))
    else:
        return container
