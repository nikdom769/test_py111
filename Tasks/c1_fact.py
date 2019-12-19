def factorial_recursive(n: int) -> int:
	"""
	Calculate factorial of number n (> 0) in recursive way
	:param n: int > 0
	:return: factorial of n
	"""
	if n < 0:
		raise ValueError
	elif n <= 1:
		return 1
	else:
		# print(n)
		return n*factorial_recursive(n - 1)




def factorial_iterative(n: int) -> int:
	"""
	Calculate factorial of number n (> 0) in iterative way
	:param n: int > 0
	:return: factorial of n
	"""
	if n < 0:
		raise ValueError
	elif n <= 1:
		return 1
	else:
		res = 1
		for i in range(1, n + 1):
			res *= i
		return res
