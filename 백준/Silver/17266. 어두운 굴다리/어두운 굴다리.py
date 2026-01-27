n = int(input())
m = int(input())
lights = list(map(int, input().split()))

answer = max(lights[0], n - lights[-1])

for i in range(m-1):
    gap = lights[i+1] - lights[i]
    need = (gap + 1) // 2
    answer = max(answer, need)

print(answer)