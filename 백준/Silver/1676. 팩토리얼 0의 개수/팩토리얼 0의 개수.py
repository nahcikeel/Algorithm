n = int(input())
result = 1
for i in range(2,n+1):
    result *= i

result = str(result)
cnt = 0

for j in result[::-1]:
    if j == '0':
        cnt += 1
    else:
        break

print(cnt)