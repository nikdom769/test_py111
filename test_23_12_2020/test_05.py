"""
Для входного списка из N строк одинаковой длины построить консенсус-строку.
"""

import collections


def cons_str(str_list: list) -> str:
    dict_ = {i: [] for i in range(len(str_list[0]))}
    res = []
    for gen in str_list:
        for ind, symb in enumerate(gen):
            dict_[ind].append(symb)
    for k, v in dict_.items():
        a = list(dict(collections.Counter(v)).items())
        if len(a) == 1:
            res.append(a[0][0])
        else:
            a.sort(key=lambda x: x[1], reverse=True)
            res.append(a[0][0])
    return "".join(res)


if __name__ == "__main__":
    dna = ['ATTA',
           'ACTA',
           'AGCA',
           'ACAA',
           ]
    print(cons_str(dna))
