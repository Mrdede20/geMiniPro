testCases = int(input())
for i in range(testCases):
    arr = list(input())
    n = len(arr)
    sum1 = 0
    sum0 = 0
    need0 = 0
    need1 = 0
    ost = 0
    for j in range(n):
        if arr[j] == '1':
            sum1 += 1
        else:
            sum0 += 1

    cost = abs(sum0 - sum1)
    for k in range(n):
        if arr[k] == '1':
            need0 += 1
        else:
            need1 += 1

        if need0 > sum0 or need1 > sum1:
            cost = n - k
            break

    print(cost)



