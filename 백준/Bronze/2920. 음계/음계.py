import sys

n = list(map(int, sys.stdin.readline().split()))

cnt = 0

for i in range(len(n)-1):
    if n[i]-1 == n[i+1]:
        cnt = 1
    elif n[i]+1 == n[i+1]:
        cnt = 2
    else:
        cnt = 3
        break

if cnt == 1:
    print('descending')

elif cnt == 2:
    print('ascending')

elif cnt == 3:
    print('mixed')