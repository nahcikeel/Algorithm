def solution(target):
    INF = 10**9

    dp = [(INF, -INF)] * (target + 1)
    dp[0] = (0, 0)

    scores = []

    # 싱글
    for i in range(1, 21):
        scores.append((i, 1))

    # 더블, 트리플
    for i in range(1, 21):
        scores.append((i * 2, 0))
        scores.append((i * 3, 0))

    # 불
    scores.append((50, 1))

    for i in range(1, target + 1):
        for score, single in scores:
            if i - score < 0:
                continue

            prev_dart, prev_single = dp[i - score]
            cand = (prev_dart + 1, prev_single + single)

            # 비교 조건
            if cand[0] < dp[i][0]:
                dp[i] = cand
            elif cand[0] == dp[i][0] and cand[1] > dp[i][1]:
                dp[i] = cand

    return list(dp[target])
