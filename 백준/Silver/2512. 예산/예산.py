n = int(input())
cities = list(map(int, input().split()))
m = int(input())

left = 0
right = max(cities)
answer = 0

while left <= right:
    mid = (left+right)//2
    total = sum(min(c,mid) for c in cities)

    if total <= m:
        answer = mid
        left = mid + 1     
    else:
        right = mid - 1 

print(answer)