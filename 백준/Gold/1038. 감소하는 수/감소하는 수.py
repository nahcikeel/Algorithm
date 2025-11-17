from itertools import combinations

N = int(input().strip())

nums = []
digits = list(range(10))

for k in range(1, 11):
    for comb in combinations(digits, k): 
        s = ''.join(str(d) for d in reversed(comb))
        nums.append(int(s))

nums.sort()

if N >= len(nums):
    print(-1)
else:
    print(nums[N])
