n = int(input())

is_prime = [True] * (n+1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(n**0.5)+1):
    if is_prime[i]:
        for j in range(i**2, n+1, i):
            is_prime[j] = False

primes = [i for i in range(2,n+1) if is_prime[i]]

left = 0
right = 0
cur_sum = 0
cnt = 0

while True:
    if cur_sum >= n:
        if cur_sum == n:
            cnt += 1
        cur_sum -= primes[left]
        left += 1
    else:
        if right >= len(primes):
            break
        cur_sum += primes[right]
        right += 1

print(cnt)