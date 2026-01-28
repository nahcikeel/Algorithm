n = int(input())
nums = [input() for _ in range(n)]

length = len(nums[0])

for k in range(1, length + 1):
    sliced = set()
    for num in nums:
        sliced.add(num[-k:])
    
    if len(sliced) == n:
        print(k)
        break
