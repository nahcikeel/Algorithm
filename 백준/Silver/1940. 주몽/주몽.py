n = int(input())
m = int(input())
nums = list(map(int, input().split()))

nums.sort()

right = n-1
left = 0
cnt = 0

while left<right:
    if (nums[left] + nums[right]) == m:
        left += 1
        right -= 1
        cnt += 1
    elif (nums[left] + nums[right]) < m:
        left += 1
    else:
        right -= 1
print(cnt)
