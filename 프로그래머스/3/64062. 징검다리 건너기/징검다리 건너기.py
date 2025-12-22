def solution(stones, k):
    left = 1
    right = max(stones)
    answer = 0

    while left <= right:
        mid = (left + right) // 2

        cnt = 0
        possible = True
        for stone in stones:
            if stone - mid < 0:
                cnt += 1
                if cnt >= k:
                    possible = False
                    break
            else:
                cnt = 0

        if possible:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer
