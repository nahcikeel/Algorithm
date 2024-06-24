li = input().split('-')

ans = []

for i in li:
    tmp = i.split('+')
    num = 0
    for j in tmp:
        num += int(j)
    ans.append(num)

n = ans[0]
for k in range(1,len(ans)):
    n -= ans[k]

print(n)