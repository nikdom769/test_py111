import random
from typing import Collection, TypeVar

_Tt = TypeVar("_Tt")


def sort(container: Collection[_Tt]) -> Collection[_Tt]:
	"""
	Sort input container with bubble sort
	:param container: container of elements to be sorted
	:return: container sorted in ascending order
	"""
	cnt_step = 0
	for i in range(len(container) - 1):
		cnt = 0
		for j in range(len(container) - 1 - i):
			if container[j] > container[j + 1]:
				container[j], container[j + 1] = container[j + 1], container[j]
				cnt = 1
		if not cnt:
			print(cnt, cnt_step)
			break
		cnt_step += 1

	return container

if __name__ == "__main__":
	arr = [random.randint(0, 10) for _ in range(10)]
	arr = [1, 2, 0, 4, 5]

	print(arr)
	print(sort(arr))