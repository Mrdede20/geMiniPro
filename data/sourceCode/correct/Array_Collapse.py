mod = 998244353

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = list(map(int, input().split(" ")))
    dp = [0 for _ in range(n+10)]
    pre = [0 for _ in range(n+10)]
    dp[0] = pre[0] = 1
    sta = [0]
    sta_sum = 1
    for i in range(1, n):
        while len(sta) > 0 and a[sta[-1]] > a[i]:
            sta_sum = (sta_sum - dp[sta.pop()] + mod) % mod
        if len(sta) == 0:
            dp[i] = (pre[i-1] + 1) % mod
        else:
            dp[i] = (pre[i-1] - pre[sta[-1]] + sta_sum + mod) % mod
        pre[i] = (pre[i-1] + dp[i]) % mod
        sta.append(i)
        sta_sum = (sta_sum + dp[i]) % mod

    ans = 0
    for i in sta:
        ans += dp[i]
    print(ans % mod)

