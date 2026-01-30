from collections import Counter

n = int(input())

for _ in range(n):
    army = list(map(int, input().split()))
    m = army[0]
    soldiers = army[1:]

    wars = Counter(soldiers)
    found = False

    for k, v in wars.items():
        if v > m//2:
            print(k)
            found = True
    if not found:
        print('SYJKGW')