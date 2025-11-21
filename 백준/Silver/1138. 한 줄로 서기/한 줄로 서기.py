n = int(input())
left = list(map(int, input().split()))

res = []
for person in range(n, 0, -1):
    k = left[person-1]
    res.insert(k, person)   # 빈 리스트에 index k 위치에 삽입
print(*res)