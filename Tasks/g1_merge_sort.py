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


def merge_new(a: Collection[_Tt], b: Collection[_Tt]) -> Collection[_Tt]:
    cont = []
    while a and b:
        if a[0] <= b[0]:
            cont.append(a.pop(0))
        elif a[0] > b[0]:
            cont.append(b.pop(0))
    if a:
        cont.extend(a)
    elif b:
        cont.extend(b)
    return cont



def sort(container: Collection[_Tt]) -> Collection[_Tt]:
    """
    Sort input container with merge sort
    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if len(container) > 1:
        return merge_new(sort(container[:len(container)//2]), sort(container[len(container)//2:]))
    else:
        return container
