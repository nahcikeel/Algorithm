import sys

n, m = map(int, input().split())
cards = list(map(int, sys.stdin.readline().split()))

max_num = 0

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1, n):
            current_sum = (cards[i] + cards[j] + cards[k])
            if current_sum <= m:
                if current_sum > max_num:
                    max_num = current_sum

print(max_num)