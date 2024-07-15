import sys
import itertools

input = sys.stdin.readline

a,b = map(int, input().split())
a = [i for i in str(a)]

arr = list(itertools.permutations(a, len(a)))
arr = list(set(arr))

num = []
for i in arr:
    if i[0] != '0':
        num.append(int(''.join(i)))

num.sort()

for k in num[::-1]:
    if k < b:
        print(k)
        break

else:
    print(-1)