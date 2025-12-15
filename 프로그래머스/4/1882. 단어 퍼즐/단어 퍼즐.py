from collections import defaultdict

def solution(strs, t):
    INF = 20001
    n = len(t)

    # 길이별로 문자열 그룹화
    by_len = defaultdict(set)
    for s in strs:
        by_len[len(s)].add(s)

    dp = [INF] * (n + 1)
    dp[0] = 0

    for i in range(n):
        if dp[i] == INF:
            continue

        for l in range(1, 6):
            if i + l > n:
                break
            if t[i:i+l] in by_len[l]:
                dp[i + l] = min(dp[i + l], dp[i] + 1)

    return dp[n] if dp[n] != INF else -1
