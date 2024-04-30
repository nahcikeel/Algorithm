n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

answer = 0

for i in range(len(a)):
    if a[i]>b[i]:
        answer += abs(a[i]-b[i])

print(answer)