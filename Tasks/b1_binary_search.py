from typing import Any, Sequence, Optional


def binary_search(elem: Any, arr: Sequence) -> Optional[int]:
	"""
	Performs binary search of given element inside of array

	:param elem: element to be found
	:param arr: array where element is to be found
	:return: Index of element if it's presented in the arr, None otherwise
	"""

	high = len(arr) - 1
	low = 0
	mid = (high - low) // 2
	while elem != arr[mid]: # low <= high :
		#if elem == arr[mid]:
		#	return mid
		if elem == arr[low]:
			return low
		elif elem == arr[high-1]:
			return high
		elif elem < arr[mid]:
			high = mid - 1
			mid -= (high - low) // 2
		else:
			low = mid + 1
			mid += (high - low) // 2
	else:
		return None


if __name__ == "__main__":
	arr = [i for i in range(100)] + [101]
	print(binary_search(101, arr))
