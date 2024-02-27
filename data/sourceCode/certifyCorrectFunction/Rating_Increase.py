from typing import List, Tuple


def rating_increase(test_cases: List[str]) -> List[str]:
    results = []
    for i in range(int(test_cases[0])):
        s = list(map(int, list(test_cases[i + 1])))
        n = len(s)
        p = str(s[0])
        r = ""
        x = 0
        if s[1] == 0:
            for i in range(1, n):
                if s[i] != 0:
                    x = i
                    break
                else:
                    p += str(s[i])
            for i in range(x, n):
                r += str(s[i])

            if int(p) < int(r):
                results.append(str(p) + " " + str(r))
            else:
                results.append("-1")
        else:
            a = s[0]
            b = ""
            for i in range(1, n):
                b += str(s[i])
            if a < int(b):
                results.append(str(a)+" "+str(b))
            else:
                results.append("-1")


    return results


def read():
    data = []
    n = input()
    data.append(n)
    for i in range(int(n)):
        data.append(input())
    return data


def write(result: List[str]):
    for item in result:
        print(item)


write(rating_increase(read()))
