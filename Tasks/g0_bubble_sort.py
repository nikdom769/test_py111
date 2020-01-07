from typing import Collection, TypeVar

_Tt = TypeVar("_Tt")


def sort(container: Collection[_Tt]) -> Collection[_Tt]:
    """
    Sort input container with bubble sort
    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if len(container) <= 1:
        return conteiner
    else:
        cnt = 0
        for i in range(len(container)):
            for j in range(len(container) - 1 - i):
                if container[j] > container[j + 1]:
                    container[j], container[j + 1] = container[j + 1], container[j]
                    cnt += 1
            if not cnt:
                return container
        return container
