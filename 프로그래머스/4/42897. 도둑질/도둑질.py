def rob(money):
    answer = 0
    
    n = len(money)
    if n == 0:
        return 0
    if n== 1:
        return money[0]
    
    dp = [0] * n
    dp[0] = money[0]
    dp[1] = max(money[0], money[1])
    
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + money[i])
    
    
    return dp[-1]


def solution(money):
    n = len(money)

    if n == 1:
        return money[0]

    case1 = rob(money[:-1])
    case2 = rob(money[1:])

    return max(case1, case2)