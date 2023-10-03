import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
m = int(input())
b = list(map(int, sys.stdin.readline().split()))

a.sort()

def binary_func(a,b):

    start = 0
    end = len(a)-1

    while start <= end:
        mid = (start+end) // 2
        
        if b == a[mid]:
            return 1
        
        elif b > a[mid]:
            start = mid +1
        
        else:
            end = mid -1
    return 0

for i in range(m):
    print(binary_func(a,b[i]))