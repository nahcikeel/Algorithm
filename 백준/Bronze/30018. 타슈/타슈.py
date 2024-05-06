n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

answer = 0

for i in range(n):
    if a[i]>b[i]:
        answer += a[i]-b[i]

print(answer)