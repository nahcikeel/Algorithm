n, k = map(int, input().split())
nums = list(map(int, input().split()))

count = [0]*(max(nums)+1)
left = 0
max_len = 0

for right in range(n):
    count[nums[right]] += 1

    while count[nums[right]] > k:
        count[nums[left]] -= 1
        left += 1
    max_len = max(max_len, (right-left+1))

print(max_len)