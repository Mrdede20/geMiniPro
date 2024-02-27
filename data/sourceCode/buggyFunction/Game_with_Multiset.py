from typing import List
from math import log2


def get(scount : List[int], v : int, sum : int) -> str:
    if v > sum:
        return 'NO'
    if v == sum:
        return 'YES'
    z = log2(v)
    if z % 1 == 0:
        if scount[int(z)] > 0:
            return 'YES'

    else:
        bry = [int(a) for a in bin(v)[2:]]
        l = len(bry)
        for i in range(l):
            f = scount[l - 1 - i]
            if f < bry[i]:
                if i == l - 1:
                    return 'NO'
                else:
                    bry[i + 1] += 2 * (bry[i] - f)
        return 'YES'


def game_with_multiset(test_cases: List[str]) -> List[str]:
    s = []
    sum = 0
    scount = [0 for i in range(50)]
    results = []
    for i in range(int(test_cases[0])):
        t, v = map(int, test_cases[i+1].split())
        if t == 1:

            sum += 2 ** v
            scount[v] += 1
        else:
            if v == 0:
                results.append('YES')
            else:
                res = get(scount, v, sum)
                results.append(res)
    return results

