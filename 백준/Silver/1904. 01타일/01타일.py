import sys

n = int(input())

MOD = 15746

if n == 1:
    print(1)
    sys.exit()

if n == 2:
    print(2) 
    sys.exit()

a,b = 1,2
for i in range(3,n+1):
    a,b = b, (a+b)%MOD

print(b)