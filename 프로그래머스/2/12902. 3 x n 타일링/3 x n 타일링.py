def solution(n):
    answer = 0
    
    # n이 홀수일때, 무조건 불가능
    if n % 2 == 1:
        return 0
    
    # n이 짝수
    
    dp = [0] * (n+1)
    dp[0] = 1
    dp[2] = 3
    
    for i in range(4, n+1, 2):
        dp[i] = 4 * dp[i-2] - dp[i-4]
    
    
    return dp[n] % 1000000007