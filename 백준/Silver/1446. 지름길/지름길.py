n,d = map(int, input().split())

shortcuts = []
for _ in range(n):
    s,e,l = map(int, input().split())
    if e<=d:
        shortcuts.append((s,e,l))

dp = [10**9]*(d+1)
dp[0] = 0

for i in range(d+1):
    if i>0:
        dp[i] = min(dp[i], dp[i-1]+1)
    
    for s,e,l in shortcuts:
        if s==i:
            dp[e] = min(dp[e], dp[s]+l)
print(dp[d])
