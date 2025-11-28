import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().strip()

count = 0
result = 0
i = 0

while i < M - 1:
    if S[i:i+3] == "IOI":
        count += 1

        if count >= N:
            result += 1
        i += 2
    else:
        count = 0
        i += 1

print(result)