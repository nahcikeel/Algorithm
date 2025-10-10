import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
num = []

for i in range(n):
    num.append([nums[i], i])

num.sort(key=lambda x: x[0])

rank = 0
ranks = [0] * n
ranks[num[0][1]] = 0

for i in range(1,n):
    if num[i][0] != num[i-1][0]:
        rank += 1
    ranks[num[i][1]] = rank

print(*ranks)

