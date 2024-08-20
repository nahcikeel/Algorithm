import sys
input = sys.stdin.readline

n,k = map(int, input().split())

bag = []

for _ in range(n):
    bag.append(list(map(int, input().split())))

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1,n+1):  # 1~4
    w = bag[i-1][0]   # 무게
    v = bag[i-1][1]   # 가치

    for j in range(1,k+1):   # 1~7
        if j >= w:
            dp[i][j] = max(v + dp[i-1][j-w], dp[i-1][j])
        else:
             dp[i][j] = dp[i-1][j]
            
print(max(dp[n]))