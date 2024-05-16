import sys

n,m = map(int, sys.stdin.readline().split())   # 나무의 개수,집에 가져갈 나무의 길이
trees = list(map(int, sys.stdin.readline().split()))

# n, m = 4,7
# trees = [20, 15, 10, 17]

low, high = 0, max(trees)
answer = 0

while low<=high:
    result = 0
    mid = (low+high)//2

    for i in trees:
        if i > mid:
            result += i-mid
    
    if result < m:
        high = mid -1
    else:
        answer = mid
        low = mid + 1

print(answer)