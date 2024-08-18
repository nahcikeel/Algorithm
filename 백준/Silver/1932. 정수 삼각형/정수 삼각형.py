import sys

input = sys.stdin.readline

n = int(input())

triangle = []

for _ in range(n):
    triangle.append(list(map(int, input().split())))


dp = [[0] for _ in range(n)]

for i in range(n):
    for j in range(i):
        dp[i].append(0)

dp[0] = triangle[0]

for row in range(1,n): # 1,2,3,4
    for idx in range(row+1):
        if idx == 0:
            dp[row][idx] = dp[row-1][idx] + triangle[row][idx]
        
        elif idx == row:
            dp[row][idx] = dp[row-1][idx-1] + triangle[row][idx]
        
        else:
            dp[row][idx] = max(dp[row-1][idx-1], dp[row-1][idx]) + triangle[row][idx]

print(max(dp[n-1]))