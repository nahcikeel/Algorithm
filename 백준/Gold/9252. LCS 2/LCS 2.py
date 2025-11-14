import sys
input = sys.stdin.readline

A = input().strip()
B = input().strip()
lenA, lenB = len(A), len(B)

# DP 테이블 생성
dp = [[0] * (lenB + 1) for _ in range(lenA + 1)]

# LCS 길이 계산
for i in range(1, lenA + 1):
    for j in range(1, lenB + 1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# LCS 문자열 역추적
i, j = lenA, lenB
result = []

while i > 0 and j > 0:
    if A[i-1] == B[j-1]:
        result.append(A[i-1])
        i -= 1
        j -= 1
    else:
        if dp[i-1][j] >= dp[i][j-1]:
            i -= 1
        else:
            j -= 1

lcs_string = ''.join(reversed(result))

# 출력
print(dp[lenA][lenB])
print(lcs_string)
