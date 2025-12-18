def solution(m, times):
    left = 1
    right = max(times) * m
    answer = right

    while left <= right:
        mid = (left + right) // 2

        total = 0
        for t in times:
            total += mid // t

        if total >= m:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer
