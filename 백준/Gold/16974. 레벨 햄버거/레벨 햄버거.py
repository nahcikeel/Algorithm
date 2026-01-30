N, X = map(int, input().split())

length = [0] * (N + 1)
patty = [0] * (N + 1)

length[0] = 1
patty[0] = 1

for i in range(1, N + 1):
    length[i] = length[i-1] * 2 + 3
    patty[i] = patty[i-1] * 2 + 1

ans = 0
n = N
x = X

while n > 0 and x > 0:
    if x == 1:
        break

    elif x <= 1 + length[n-1]:
        x -= 1
        n -= 1

    elif x == 2 + length[n-1]:
        ans += patty[n-1] + 1
        break

    elif x <= 2 + 2 * length[n-1]:
        ans += patty[n-1] + 1
        x -= (2 + length[n-1])
        n -= 1

    else:
        ans += patty[n]
        break

if n == 0 and x > 0:
    ans += 1

print(ans)
