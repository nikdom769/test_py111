import random
from typing import Collection, TypeVar

_Tt = TypeVar("_Tt")


def sort_old(container: Collection[_Tt]) -> Collection[_Tt]:
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
        return sort_old(first) + [pivot] + sort_old(last)
    else:
        return container


def sort_old_new(container: Collection[_Tt]) -> Collection[_Tt]: # не работает когда в списке есть одинаковые элементы
    """
    Sort input container with quick sort
    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if len(container) > 1:
        pivot = random.choice(container)
        left = [i for i in container if i < pivot]
        right = [i for i in container if i >= pivot]
        return sort_old_new(left) + sort_old_new(right)
    else:
        return container




def sort(container: Collection[_Tt]) -> Collection[_Tt]: #  не работает когда в списке есть одинаковые элементы
    """
    Sort input container with quick sort
    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if len(container) > 1:
        #pivot = container[len(container)//2]
        pivot = random.choice(container)
        i = 0
        j = len(container) - 1
        while i < j:
            if container[i] < pivot:
                i += 1
            elif container[j] > pivot:
                j -= 1
            else:
                container[i], container[j] = container[j], container[i]
        return sort(container[0:container.index(pivot)]) + sort(container[container.index(pivot):])
    else:
        return container




if __name__ == "__main__":
    arr = [random.randint(-100, 100) for _ in range(10)]
    print(arr)
    
    print("Проверка функции sort_old")
    assert sort_old(arr) == sorted(arr), f"{sort_old(arr)} \n {sorted(arr)}"

    print("Проверка функции sort_old_new")
    assert sort_old_new(arr) == sorted(arr), f"{sort_old_new(arr)} \n {sorted(arr)}"
    
    print("Проверка функции sort")
    assert sort(arr) == sorted(arr), f"{sort(arr)} \n {sorted(arr)}"

