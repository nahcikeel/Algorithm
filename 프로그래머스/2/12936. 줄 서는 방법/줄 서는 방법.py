import math

def solution(n, k):
    nums = list(range(1, n + 1))
    answer = []
    k -= 1  # 0부터 시작하게 맞춤

    while n > 0:
        fact = math.factorial(n - 1)
        idx = k // fact

        answer.append(nums[idx])
        nums.pop(idx)

        k %= fact
        n -= 1

    return answer
