from collections import defaultdict

n = int(input())
nums = list(map(int, input().split()))

count = defaultdict(int)
left = 0
max_len = 0

for right in range(n):
    count[nums[right]] += 1
    
    while len(count) > 2:
        count[nums[left]] -= 1
        if count[nums[left]] == 0:
            del count[nums[left]]
        left += 1
    
    max_len = max(max_len, right-left+1)

print(max_len)