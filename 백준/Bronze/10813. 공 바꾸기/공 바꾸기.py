n,m = map(int, input().split())

answer = list(range(1, n+1))

for _ in range(m):
    a, b = map(int, input().split())
    answer[a-1], answer[b-1] = answer[b-1], answer[a-1]

for i in answer:
    print(i, end =' ')