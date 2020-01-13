import random
from typing import Collection, TypeVar

_Tt = TypeVar("_Tt")


def merge(left: list, right: list) -> list:
	res = []
	while left and right:
		if left[0] <= right[0]:
			res.append(left.pop(0))
		else:
			res.append(right.pop(0))
	while left:
		res.extend(left)
		left = []
	while right:
		res.extend(right)
		right = []
	return res


def sort(container: Collection[_Tt]) -> Collection[_Tt]:
	"""
	Sort input container with merge sort
	:param container: container of elements to be sorted
	:return: container sorted in ascending order
	"""
	cnt = 0
	if len(container) <= 1:
		return container
	else:
		middle = len(container) // 2
		#print(f"{'=' * 5} {cnt} {'=' * 5}")
		return merge(sort(container[:middle]), sort(container[middle:]))


if __name__ == "__main__":
	arr = [random.randint(0, 10) for _ in range(11)]
	print(arr)
	print(sort(arr))
