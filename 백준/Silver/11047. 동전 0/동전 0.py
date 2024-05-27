n, k = map(int, input().split())
coins = []

for _ in range(n):
    coins.append(int(input()))

cnt = 0

coins.sort(reverse=True)

for coin in coins:
    if coin <= k:
        cnt += (k//coin)
        k = (k%coin)
        
        if k == 0:
            break

print(cnt)