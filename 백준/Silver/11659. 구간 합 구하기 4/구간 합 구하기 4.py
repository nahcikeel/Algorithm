import sys
input = sys.stdin.readline

n,m = map(int, input().split())
num = list(map(int, input().split()))

initSum = [0]
temp = 0

for i in num:
    temp+=i
    initSum.append(temp)

for _ in range(m):
    a,b = map(int, input().split())
    print(initSum[b] - initSum[a-1])