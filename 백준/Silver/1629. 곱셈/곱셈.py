def abc(a,b,c):
    if b==1:
        return a%c
    elif b%2==0:
        return abc(a,b//2,c)**2%c
    else:
        return abc(a,b//2,c)**2*a%c

num = list(map(int, input().split()))

print(abc(num[0],num[1],num[2]))