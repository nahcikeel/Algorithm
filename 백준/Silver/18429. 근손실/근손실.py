import sys
import itertools

input = sys.stdin.readline

n,k = map(int, input().split())
a = list(map(int, input().split()))

cnt = 0
arr = list(itertools.permutations(a, len(a)))

for i in arr:
    hp = 500
    val = True
    for j in i:
        hp += j-k
        if hp < 500:
            val = False
            break
    if val:
        cnt += 1

print(cnt)