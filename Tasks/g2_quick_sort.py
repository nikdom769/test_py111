import random
from typing import Collection, TypeVar

_Tt = TypeVar("_Tt")


def partition(A):
	pivot = A[len(A) // 2]
	i = 0
	j = len(A) - 1
	while i <= j:
		if A[i] < pivot:
			i += 1
		elif A[j] >= pivot:
			j -= 1
		else:
			A[i], A[j] = A[j], A[i]
	return A



def sort(container: Collection[_Tt]) -> Collection[_Tt]:
	"""
	Sort input container with quick sort
	:param container: container of elements to be sorted
	:return: container sorted in ascending order
	"""
	i = 0
	j = len(container) - 1
	pivot = container[len(container) // 2]
	left = []
	right = []

	if len(container) <= 1:
		return container
	else:
		while i < j:
			if container[i] < pivot:
				left.append(container[i])
			else:
				right.append(container[i])
			if container[j] >= pivot:
				right.append(container[j])
			else:
				left.append(container[j])
			i += 1
			j -= 1
		return sort(left) + [pivot] + sort(right)


if __name__ == "__main__":
	arr = [random.randint(0, 10) for _ in range(11)]
	#assert sort(arr) == arr.sort()
	print(arr)
	print(sort(arr))