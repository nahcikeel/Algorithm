n = int(input())

cnt = 0

while True:
    if n%5 ==0: 
        cnt += n//5
        print(cnt)
        break

    elif n in [1,3]:
       print(-1)
       break

    else:
        n -= 2
        cnt += 1
