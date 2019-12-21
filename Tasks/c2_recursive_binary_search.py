from typing import Any, Sequence, Optional


def binary_search(elem: Any, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)
    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    ind = len(arr) // 2
    if elem == arr[ind]:
        return ind
    elif len(arr) <= 1:
        return None
    else:
        if elem > arr[ind]:
            res = binary_search(elem, arr[ind:])
            return (ind + res) if res else None 
        else:
            return binary_search(elem, arr[:ind])


if __name__ == "__main__":
    arr = [i for i in range(100)] + [101]

    print(binary_search(-1, arr))
    print(binary_search(100, arr))
    print(binary_search(95, arr))
    print(binary_search(0, arr))
    print(binary_search(101, arr))
