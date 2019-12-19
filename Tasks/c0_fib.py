
def fib_recursive(n: int) -> int:
	"""
	Calculate n-th number of Fibonacci sequence using recursive algorithm
	:param n: number of item
	:return: Fibonacci number
	"""

	if n < 0:
		raise ValueError
	elif n == 0:
		return 0
	elif 0 < n <= 2:
		return 1
	else:
		return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n: int) -> int:
	"""
	Calculate n-th number of Fibonacci sequence using iterative algorithm
	:param n: number of item
	:return: Fibonacci number
	"""
	if n < 0:
		raise ValueError
	else:
		numb = [0, 1]
		for i in range(2, (n + 1)):
			numb.append(numb[i - 1] + numb[i - 2])
		return numb[n]

if __name__ == "__main__":
	#print(fib_recursive(-35))
	print(fib_iterative(-1))