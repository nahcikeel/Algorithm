from itertools import combinations
from collections import Counter

n,s = map(int, input().split())
nums = list(map(int, input().split()))

def sum_count(nums):
    sums = []
    n = len(nums)
    for i in range(1,n+1):
        for comb in combinations(nums, i):
            sums.append(sum(comb))
    return Counter(sums)

counter_sum = sum_count(nums)

print(counter_sum[s])