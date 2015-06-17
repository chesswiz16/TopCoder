__author__ = 'Tiger'

def country_group_hard(a):
    n = len(a)
    dp = [False for x in range(n + 1)]
    dp[0] = True
    for i in range(1, n + 1):
        for length in range(1, n + 1):
            ok = True
            for j in range(i - length, i):
                if a[j] is not len and a[j] is not 0:
                    ok = False
        if ok:
            dp[i] += dp[i - length]
            dp[i] = min(dp[i], 1000)
    return "Sufficient" if dp[n] == 1 else "Insufficient"

print(country_group_hard([0, 2, 3, 0, 0]))