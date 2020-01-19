from typing import Sequence #Optional, Sequence


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
        prefix_tbl = [0 for _ in range(len(prefix_str))]
        for i in range(len(prefix_str)):
            for j in range(i):
                if prefix_str[0:j] == prefix_str[i - j:i]:
                    prefix_tbl[i - 1] = j
        return prefix_tbl

    prefix_tbl = prefix_fun(substr)
    i = 0
    j = 0
    
    while i < len(inp_string):
        if inp_string[i] == substr[j]:
            i += 1
            j += 1
            if j == len(substr) and i <= len(inp_string):
                return i - j
        elif j <= 0:
            i += 1
        elif j > 0:
            j = prefix_tbl[j - 1]
      


if __name__ == "__main__":
    a = "ATGATC"
    b = "ATTATGATGATC"
    print(a)
    print(b)
    print(kmp_algo(b, a))

