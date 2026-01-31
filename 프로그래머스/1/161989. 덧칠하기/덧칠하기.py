def solution(n, m, section):
    cnt = 0
    paint_end = 0

    for i in range(len(section)):
        if section[i] > paint_end:
            cnt += 1
            paint_end = section[i] + m - 1

    return cnt
