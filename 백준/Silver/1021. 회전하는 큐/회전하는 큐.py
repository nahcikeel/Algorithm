from collections import deque

n,m = map(int, input().split())
targets = list(map(int, input().split()))

answer = 0
nums = deque(range(1,n+1))

for t in targets:
    idx = nums.index(t)

    if idx <= len(nums)//2:
        nums.rotate(-idx)
        answer += idx
    else:
        nums.rotate(len(nums)-idx)
        answer += len(nums)-idx
    nums.popleft()

print(answer)