import sys

input = sys.stdin.readline

n, k = map(int, input().split())
fish = [0] * 1000001

for _ in range(n):
    g, x = map(int, input().split())
    fish[x] = g

window_sum = sum(fish[:2*k +1])
max_sum = window_sum

for i in range(2*k +1, 1000001):
    window_sum += fish[i] - fish[i - (2*k + 1)]
    max_sum = max(max_sum, window_sum)

print(max_sum)