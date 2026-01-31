def div_cnt(num):
    cnt = 0
    i = 1
    while i * i <= num:
        if num % i == 0:
            cnt += 1
            if i != num // i:
                cnt += 1
        i += 1
    return cnt


def solution(number, limit, power):
    answer = 0

    for i in range(1, number + 1):
        d = div_cnt(i)
        if d > limit:
            answer += power
        else:
            answer += d

    return answer
