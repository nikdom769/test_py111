from typing import Optional, Sequence


def kmp_algo(inp_string: str, substr: str): # -> Optional(int):
	"""
	Implementation of Knuth-Morrison-Pratt algorithm

	:param inp_string: String where substr is to be found (haystack)
	:param substr: substr to be found in inp_string (needle)
	:return: index where first occurrence of substr in inp_string started or None if not found
	"""

	def prefix_fun(prefix_str: str) -> Sequence[int]:
		"""
		Prefix function for KMP
		:param prefix_str: dubstring for prefix function
		:return: prefix values table
		"""
		prefix_tabl = []
		for i in range(len(prefix_str)):
			for j in range(i - 1):
				if prefix_str[0:j] == prefix_str[i-j:i]:
					prefix_tabl.insert(i, j)

		print(prefix_tabl) #(prefix_str)
		return prefix_tabl

	prefix_fun(substr)
	#print(inp_string, substr, prefix_fun)
	#return None


str = "abcabcd"
str1 = "abcabcddabcabcd"
str = 'aaa'
kmp_algo(str1, str)
